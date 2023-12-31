# Generated by Django 4.1.7 on 2023-05-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0006_producto_foto_alter_producto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='detalles',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
