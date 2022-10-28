class Basket:
    """
    Base class for basket
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {'number': 123123}
        self.basket = basket
