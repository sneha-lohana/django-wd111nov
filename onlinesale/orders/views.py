from django.shortcuts import render
from django.http import HttpResponse
from carts.models import Cart
from billing.models import BillingProfile
from .models import Order
from accounts.forms import SignInForm
from addresses.forms import AddressForm
from addresses.models import Address

def create_order(request):
    loginform = SignInForm()
    addressForm = AddressForm()
    context = {'loginform':loginform, 'addressForm':addressForm}
    cart_obj = Cart.objects.new_or_get(request)
    bill_obj = BillingProfile.objects.get_or_new(request)
    if cart_obj and bill_obj:
        order_obj = Order.objects.get_or_new(cart_obj, bill_obj)
        context['order_obj'] = order_obj
        add_list = Address.objects.filter(billing_profile=bill_obj)
        context['addList'] = add_list
    return render(request, "orders/placeorder.html", context)

def received_payment(request):
    print(request.POST)
    orderid = request.POST.get("shopping_order_id")
    payid = request.POST.get("razorpay_payment_id")
    order_obj = Order.objects.filter(order_id=orderid).first()
    if order_obj:
        order_obj.razor_pay_id = payid
        order_obj.status = "paid"
        order_obj.save()
        del request.session['cart_id']
        context = {'orderid':orderid, 'payid':payid}
    return render(request, "orders/success.html", context)