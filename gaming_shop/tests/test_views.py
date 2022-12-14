from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from unittest import skip
from django.contrib.auth.models import User
from gaming_shop.models import Category, Product
from datetime import date
from django.http import HttpRequest
from gaming_shop.views import index


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.user1 = User.objects.create(username="admin")
        self.category1 = Category.objects.create(name='Action', slug='Action')
        self.product1 = Product.objects.create(category_id=self.category1.id, created_by_id=self.user1.id, title="test game", description="a test game",
                                            slug='test_game', price='20.00', image='test', developer='test', publisher='test',
                                            in_stock=True, is_active=True, release_date=str(date.today()))

        self.product2 = Product.objects.create(category_id=self.category1.id, created_by_id=self.user1.id, title="test game2", description="a test game",
                                            slug='test_game2', price='30.00', image='test', developer='test', publisher='test',
                                            in_stock=True, is_active=True, release_date=str(date.today()))

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """

        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("shop:category_list", args=['Action']))
        self.assertEqual(response.status_code, 200)

    def test_products_index(self):
        products = Product.objects.all()
        response = self.c.get(reverse('shop:index'))
        self.assertQuerysetEqual(response.context['products'], products)
        self.assertEqual(response.status_code, 200)


    def test_product_item_page(self):
        product = Product.objects.first()
        response = self.c.get(reverse("shop:product_item", args=[product.slug]))
        self.assertEqual(response.context['product'], product)
        self.assertEqual(response.status_code, 200)
        #TODO: amend test so that coverage sees above test as passing
        #TODO: may need to fix this test

    #TODO: add test for category_list view

    def test_index_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('\n\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/game/test_game')
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertTrue(html.startswith('\n\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST="none.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST="gamestation.com")
        self.assertEqual(response.status_code, 200)
