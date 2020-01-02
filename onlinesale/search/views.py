from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductListView(ListView):
    template_name = 'products/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data()
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('q', None):
            qs = Product.objects.search(self.request.GET.get('q'))
        else:
            qs = Product.objects.all()
        return qs
