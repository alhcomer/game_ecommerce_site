from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .basket import Basket
from gaming_shop.models import Product


def basket_summary(request):

    return render(request, 'basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        platform = str(request.POST.get('platform'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_qty, platform=platform)
        basket_qty = basket.__len__()
        response = JsonResponse({'quantity': basket_qty})
        return response

def basket_remove(request):
    basket = Basket(request)
    if request.POST.get('action') == 'POST':
        product_id = str(request.POST.get('productid'))
        print(product_id)
        basket.remove(product_id=product_id)
        basket_qty = basket.__len__()
        basket_price = basket.get_total_price()
        response = JsonResponse({'quantity': basket_qty, 'totalprice': basket_price, 'productid': product_id})
        return response