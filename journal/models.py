# journal/models.py
from django.db import models
from product.models import Product


class Journal(models.Model):
    product = models.ForeignKey(Product, related_name='images', blank=True,
                                null=True, default=None, on_delete=models.CASCADE)
    cnt = models.IntegerField(default=1)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    goods_in = 'Приход'
    goods_out = 'Уход'
    GOODS_OPERATION_CHOICES = (
        (goods_in, 'Приход'),
        (goods_out, 'Уход'),
    )
    goods_operation = models.CharField(max_length=13, choices=GOODS_OPERATION_CHOICES, default=goods_in)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Журнал прихода/ухода'
        verbose_name_plural = 'Журнал прихода/ухода'
