from django.shortcuts import get_object_or_404
from gaming_shop.models import Product

class Basket:
    """
    Base class for basket
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket
        

    def add(self, product, quantity):
        product_id = product.id
        if product_id not in self.basket:
            # NEED TO ADD PLATFORM OF PRODUCT TO BASKET
            self.basket[str(product_id)] = {'price': str(product.price), 'quantity': int(quantity), 'image_url': str(product.image.url), 'title': str(product.title)}
        self.session.modified = True
    
    def __len__(self):
        """
        Counts quantity of items in basket
        """
        return sum(item['quantity'] for item in self.basket.values())
    
    def remove(self, product_id):
        del self.basket[str(product_id)]
        self.save()

    def save(self):
        self.session.modified = True
    
    def get_total_price(self):
        total_price = 0
        print(self.basket.values())
        for value in self.basket.values():
            item_price = float(value['price']) * value['quantity']
            total_price += item_price
        return total_price
