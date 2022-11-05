from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .basket import Basket
from gaming_shop.models import Product
from django.core import serializers
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize


def basket_summary(request):
    return render(request, 'basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_qty)
        
        response = JsonResponse({'test': 'data'})
        return response