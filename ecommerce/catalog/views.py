from catalog.models import Item
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeView(ListView):
    model = Item
    template_name = 'home.html'



# def home(request):
#     return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def checkout(request):
    return render(request, 'checkout.html')
