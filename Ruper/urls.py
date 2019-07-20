from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
        path(r'index', views.register_view, name='index'),
        path(r'cart',views.cart_view, name="cart")

]