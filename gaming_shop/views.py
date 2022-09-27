from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Platform

def index(request):
    products = Product.objects.all()
    return render(request, 'gaming_shop/index.html', {'products': products})
