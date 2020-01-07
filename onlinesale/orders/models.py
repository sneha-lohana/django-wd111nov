from django.db import models
from billing.models import BillingProfile
from addresses.models import Address
from carts.models import Cart
from django.db.models.signals import pre_save
from products.utils import unique_orderid_generator
from decimal import Decimal

ORDER_STATUS_CHOICES = (('created', 'Order is created'),
('paid','You have paid for order'))

class OrderManager(models.Manager):
    def get_or_new(self, cart_obj, bill_obj):
        order_obj = self.get_queryset().filter(cart=cart_obj, billingProfile=bill_obj, status='created').first() or None
        if order_obj is None:
            order_obj = self.get_queryset().create(cart=cart_obj, billingProfile=bill_obj)
        if order_obj.order_total != cart_obj.total:
            order_obj.update_order(cart_obj)
        return order_obj

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True) #ASFGHH3345678SDFGHJK
    billingProfile = models.ForeignKey(BillingProfile, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, default='created', choices=ORDER_STATUS_CHOICES)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0) 
    total = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)  #GST

    objects = OrderManager()

    def __str__(self):
        return self.order_id

    def update_order(self, cart_obj):
        if self.order_total != cart_obj.total:
            self.order_total = cart_obj.total
            self.total = round(self.order_total * Decimal(1.18), 2)
            self.save()

def orderid_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.order_id is None or instance.order_id=="":
        instance.order_id = unique_orderid_generator(instance)

pre_save.connect(orderid_pre_save_receiver, sender=Order)