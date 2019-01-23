# product/admin.py

from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'is_new')
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = list_display = ('id', 'product')

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)

