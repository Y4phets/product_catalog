"""
Перед тестированием закомментировать весь REST_FRAMEWORK в settings.py
"""
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product
from product.serializers import ProductSerializer


# initialize the APIClient app
client = Client()


class GetAllProductsTest(TestCase):

    def setUp(self):
        Product.objects.create(
            name='Apple', sku=3321473019423, created_at='2019-01-22T12:37:47',
            updated_at='2019-01-22T14:37:47', is_new=True)
        Product.objects.create(
            name='Orange', sku=9921473019423, created_at='2019-01-22T13:37:47',
            updated_at='2019-01-22T15:37:47', is_new=False)

    def test_get_all_products(self):
        response = client.get(reverse('get_post_products'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):

    def setUp(self):
        self.apple = Product.objects.create(
            name='Apple', sku=3321473019423, created_at='2019-01-22T12:37:47',
            updated_at='2019-01-22T14:37:47', is_new=True)
        self.orange = Product.objects.create(
            name='Orange', sku=9921473019423, created_at='2019-01-22T13:37:47',
            updated_at='2019-01-22T15:37:47', is_new=False)

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': self.apple.pk}))
        product = Product.objects.get(pk=self.apple.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "name": "Apple",
            "sku": "371421531324",
            "created_at": "2019-01-22T12:37:47",
            "updated_at": "2019-01-22T15:37:47",
            "is_new": False,
        },
        self.invalid_payload = {
            "name": "",
            "sku": "371442531324",
            "created_at": "",
            "updated_at": "",
            "is_new": False,
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductTest(TestCase):

    def setUp(self):
        self.apple = Product.objects.create(
            name='apple', sku=371421531324, is_new=True)
        self.orange = Product.objects.create(
            name='orange', sku=9921473019423, is_new=False)

        self.valid_payload = {
            "name": "apple",
            "sku": "371421531324",
            "is_new": False,
        },
        self.invalid_payload = {
            "name": "",
            "sku": "371442531324",
            "is_new": False,
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.apple.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.apple.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):

    def setUp(self):
        self.apple = Product.objects.create(
            name='apple', sku=371421531324, created_at='2019-01-22T12:37:47',
            updated_at='2019-01-22T14:37:47', is_new=True)
        self.orange = Product.objects.create(
            name='orange', sku=9921473019423, created_at='2019-01-22T13:37:47',
            updated_at='2019-01-22T15:37:47', is_new=False)

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.apple.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
