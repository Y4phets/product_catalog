from django.test import TestCase
from product.models import Product


class ProductTest(TestCase):

    def setUp(self):
        Product.objects.create(
            name='Apple', sku=3321473019423, created_at='2019-01-22T12:37:47',
            updated_at='2019-01-22T14:37:47', is_new=True)
        Product.objects.create(
            name='Orange', sku=9921473019423, created_at='2019-01-22T13:37:47',
            updated_at='2019-01-22T15:37:47', is_new=False)

    def test_product(self):
        product_apple = Product.objects.get(sku=3321473019423)
        product_orange = Product.objects.get(sku=9921473019423)
        self.assertEqual(
            product_apple.get_name(), "SKU=3321473019423 belongs to Apple.")
        self.assertEqual(
            product_orange.get_name(), "SKU=9921473019423 belongs to Orange.")
