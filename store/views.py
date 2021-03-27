from django.shortcuts import render
from .models import *


def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def faq(request):
    context = {}
    return render(request, 'store/faq.html', context)

def register(request):
    context = {}
    return render(request, 'store/register.html', context)
