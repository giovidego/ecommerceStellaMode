# Generated by Django 4.1.7 on 2023-05-19 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0004_remove_producto_id_producto_sku'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
