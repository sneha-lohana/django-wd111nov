from django.db import models
from billing.models import BillingProfile

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_to_name = models.CharField(max_length=120)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='India')
    state           = models.CharField(max_length=120)
    pin_code     = models.CharField(max_length=120)