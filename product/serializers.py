# product/serializers.py
from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'image', 'name', 'sku', 'created_at', 'updated_at', 'is_new')
        model = models.Product
