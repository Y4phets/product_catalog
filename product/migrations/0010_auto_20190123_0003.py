# Generated by Django 2.0.7 on 2019-01-22 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20190122_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
    ]