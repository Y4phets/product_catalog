# journal/serializers.py
from rest_framework import serializers
from . import models


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'product', 'cnt', 'customer_email', 'created_at', 'updated_at', 'goods_operation')
        model = models.Journal
