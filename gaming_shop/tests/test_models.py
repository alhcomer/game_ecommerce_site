from email.mime import image
from django.test import TestCase
from datetime import date

from gaming_shop.models import Category, Product, Platform
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data = Category.objects.create(name='test', slug='test')

    def test_category_model_entry(self):
        """
        Test Category model insertion/types/field attributes
        """
        data = self.data
        self.assertTrue(isinstance(data, Category))
        

    def test_category_model_entry_name(self):
        """
        Test Category model return name
        """
        data = self.data
        self.assertEqual(str(data), 'test')


class TestProductModel(TestCase):

    def setUp(self):

        self.category1 = Category.objects.create(name='action', slug='action')
        self.user1 = User.objects.create(username='admin')
        self.platform1 = Platform.objects.create(name='Xbox One')
        self.data = Product.objects.create(category_id=self.category1.id, created_by_id=1, title="test game", description="a test game",
                                            slug='test game', price='20.00', image='test', developer='test', publisher='test',
                                            in_stock=True, is_active=True, release_date=str(date.today()))
        
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """

        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'test game')