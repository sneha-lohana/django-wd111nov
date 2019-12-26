"""onlinesale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_page, about_page, contact_page
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_page, signin_page, signout_page
from django.conf.urls import include

urlpatterns = [
    path("product/", include(('products.urls', 'products'),namespace="product")),
    path('admin/', admin.site.urls),
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
    path("register/", register_page, name="register"),
    path("signin/", signin_page, name="signin"),
    path("signout/", signout_page, name="signout"),
    path("cart/", include(('carts.urls', 'carts'), namespace="cart"))
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
