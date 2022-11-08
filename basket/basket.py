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
        print(basket)
        

    def add(self, product, quantity):
        product_id = product.id
        if product_id not in self.basket:
            self.basket[str(product_id)] = {'price': str(product.price), 'quantity': int(quantity), 'image_url': str(product.image.url)}

        self.session.modified = True
    
    def __len__(self):
        """
        Counts quantity of items in basket
        """
        return sum(item['quantity'] for item in self.basket.values())

