from django.test import TestCase, Client
from unittest import skip
from django.contrib.auth.models import User
from gaming_shop.models import Category, Product

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """

        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)