from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Platform

def index(request):
    products = Product.objects.all()
    return render(request, 'gaming_shop/index.html', {'products': products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product_item(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'gaming_shop/products/game_item.html', {'product': product})