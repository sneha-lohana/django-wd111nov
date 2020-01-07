from django.urls import path
from .views import add_address

urlpatterns = [
path("add/", add_address, name="add"),
]