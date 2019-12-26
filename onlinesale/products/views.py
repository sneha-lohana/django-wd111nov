from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from carts.models import Cart

# Create your views here.
def product_list(request):
    object_list = Product.objects.all()
    context = {'object_list': object_list}
    return render(request, 'products/list.html', context)

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     prodList  = Product.objects.all()
    #     context = {'object_list':prodList}
    #     return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        cart_obj = Cart.objects.new_or_get(self.request)
        context['in_cart'] = context['object'] in cart_obj.products.all()
        return context
