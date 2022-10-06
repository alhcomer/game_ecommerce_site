from django.urls import reverse
from django.test import TestCase, Client
from unittest import skip
from django.contrib.auth.models import User
from gaming_shop.models import Category, Product

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.data = Category.objects.create(name='Action', slug='Action')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """

        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("shop:category_list", args=['Action']))
        self.assertEqual(response.status_code, 200)