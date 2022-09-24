from django.test import TestCase

from gaming_shop.models import Category, Product, Platform


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data = Category.objects.create(name='test', slug='test')

    def test_category_model_entry(self):
        """
        Test Category model insertion/types/field attributes
        """
        data = self.data
        self.assertTrue(isinstance(data, Category))