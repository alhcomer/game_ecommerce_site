from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .basket import Basket
from gaming_shop.models import Product
from django.core import serializers
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

# class LazyEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, YourCustomType):
#             return str(obj)
#         return super().default(obj)

def basket_summary(request):
    return render(request, 'basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        # TODO: must make product object json serializable
        # print(product)
        # product = serialize('json', product, cls=LazyEncoder)
        basket.add(product=product)
        response = JsonResponse({'test': 'data'})
        return response