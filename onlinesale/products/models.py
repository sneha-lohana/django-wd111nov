from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import Q

class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | Q(description__icontains=query) | Q(price__iexact=query) | Q(tag__title__icontains=query))
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().search(query)

class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="products")
    price = models.DecimalField(default=10, max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_abs_url(self):
        return reverse('product:detail', kwargs={'slug':self.slug})

    def get_abs_url1(self):
        return reverse('product:detail', kwargs={'pk':self.id})

def product_slug_pre_save_receiver(sender, instance,*args, **kwargs):
    instance.slug = unique_slug_generator(instance)

pre_save.connect(product_slug_pre_save_receiver, sender=Product)