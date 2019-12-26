from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class CartManager(models.Manager):
    def new_or_get(self, request):
        cartid = request.session.get('cart_id', None)
        if cartid is not None:
            cart_obj = Cart.objects.filter(id=cartid).first()
        elif request.user.is_authenticated:
            cart_obj = Cart.objects.create(user=request.user)
            request.session['cart_id'] = cart_obj.id
        else:
            cart_obj = Cart.objects.create()
            request.session['cart_id'] = cart_obj.id
        return cart_obj

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    created   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)