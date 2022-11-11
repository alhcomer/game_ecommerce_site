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
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_qty)
        basket_quantity = basket.__len__()
        response = JsonResponse({'quantity': basket_quantity})
        print(basket.basket)
        return response

def basket_remove(request): 
    basket = Basket(request)
    if request.POST.get('action') == 'DELETE':
        product_id = int(request.POST.get('productid'))
        return product_id