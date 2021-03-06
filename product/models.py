# product/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_new = models.BooleanField(default=True)

    def get_name(self):
        return 'SKU=' + self.sku + ' belongs to ' + self.name + '.'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, related_name="image",
                                null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
