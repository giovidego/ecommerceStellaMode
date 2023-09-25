from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    #list_display=("sku","nombre","marca")
    search_fields=("sku", "nombre", "marca")

admin.site.register(Producto, ProductoAdmin)
