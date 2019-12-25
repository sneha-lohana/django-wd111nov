from django.urls import path
from .views import product_list, ProductListView, ProductDetailView

urlpatterns = [
    path("", product_list, name="fbv"),
    path("cbv/", ProductListView.as_view(), name="cbv"),
    # path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("<str:slug>/", ProductDetailView.as_view(), name="detail"),
]
