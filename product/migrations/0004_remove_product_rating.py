# Generated by Django 3.2.25 on 2024-04-14 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
