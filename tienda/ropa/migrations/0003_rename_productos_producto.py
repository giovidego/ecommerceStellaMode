# Generated by Django 4.1.7 on 2023-05-18 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0002_alter_productos_cantidad_alter_productos_precio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
