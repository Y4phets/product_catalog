# product/serializers.py
from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = models.Product
        fields = ('id', 'image', 'name', 'sku', 'created_at', 'updated_at', 'is_new')

    def get_validation_exclusions(self):
        exclusions = super(ProductSerializer, self).get_validation_exclusions()
        return exclusions + ['image']
