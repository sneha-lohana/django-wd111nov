from django.shortcuts import render, redirect
from .forms import AddressForm
from billing.models import BillingProfile
from orders.models import Order
from carts.models import Cart
from django.utils.http import is_safe_url
from .models import Address

# Create your views here.
def add_address(request):
    redirect_path = request.POST.get('next_url') or None
    form = AddressForm(request.POST or None)
    if form.is_valid():
        add_obj = form.save(commit=False)
        bill_obj = BillingProfile.objects.get_or_new(request)
        add_obj.billing_profile = bill_obj
        add_obj.save()
        add_address_to_order(request, add_obj)
        if redirect_path:
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
    return redirect("home")

def attach_address(request):
    redirect_path = request.POST.get('next_url') or None
    addid = request.POST.get('address')
    add_obj = Address.objects.filter(id=addid).first()
    add_address_to_order(request, add_obj)
    if redirect_path:
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
    return redirect("home")

def add_address_to_order(request, add_obj):
    cart_obj = Cart.objects.new_or_get(request)
    order_obj = Order.objects.get_or_new(cart_obj, add_obj.billing_profile)
    order_obj.address = add_obj
    order_obj.save()

