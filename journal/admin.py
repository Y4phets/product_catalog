# journal/admin.py

from django.contrib import admin
from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cnt', 'customer_email', 'created_at', 'updated_at', 'goods_operation')

    class Meta:
        model = Journal


admin.site.register(Journal, JournalAdmin)
