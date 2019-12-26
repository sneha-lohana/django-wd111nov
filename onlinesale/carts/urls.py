from django.urls import path
from .views import update_cart
urlpatterns = [
    path("update/", update_cart, name="update"),
]