from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
]