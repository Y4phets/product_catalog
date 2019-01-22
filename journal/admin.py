# journal/admin.py

from django.contrib import admin
from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Journal._meta.fields]

    class Meta:
        model = Journal


admin.site.register(Journal, JournalAdmin)
