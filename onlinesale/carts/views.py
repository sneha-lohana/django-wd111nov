from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart

def update_cart(request):
    cart_obj = Cart.objects.new_or_get(request)
    if request.method == 'POST':
        prodid = request.POST.get('prodid')
        if prodid:
            prod_obj = Product.objects.filter(id=prodid).first()
            #query set select * from carts_cart_products where cart_id = cartid
            if prod_obj in cart_obj.products.all():
                #remove
                cart_obj.products.remove(prod_obj)
            else:
                #add
                cart_obj.products.add(prod_obj)
    return redirect(prod_obj.get_abs_url())
