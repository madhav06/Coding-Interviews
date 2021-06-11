
from django.shortcuts import render


# Create your views here.
def catalog(request):
    context = {}
    return render(request, 'catalog/catalog.html', context)

def cart(request):
    context = {}
    return render(request, 'catalog/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'catalog/checkout.html', context)
