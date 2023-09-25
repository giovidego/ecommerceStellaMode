from django.shortcuts import render, redirect
from .carro import Carro
from ropa.models import Producto
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def agregar_producto(request, pk):
    if request.method == 'POST':
        cantidad_producto = request.POST.get('cantidad_p')
        carro = Carro(request)
        producto = Producto.objects.get(sku=pk)

        carro.agregar(producto,cantidad_producto)
    
        return redirect("index")

def eliminar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.eliminar(producto)
    
    return redirect("carro")

def sumar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.sumar_producto(producto=producto)
    
    return redirect("carro")

def restar_producto(request,pk):
    carro= Carro(request)
    producto= Producto.objects.get(sku=pk)

    carro.restar_producto(producto=producto)
    
    return redirect("carro")


def limpiar_carroproducto(request):
    carro= Carro(request)
    carro.limpiar_carro()
    
    return redirect("carro")