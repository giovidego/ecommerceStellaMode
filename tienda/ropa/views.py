from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ropa.models import Producto 
from pedidos.models import LineaPedido, Pedido


# Create your views here.
def index(request):
    print("estoy en index")
    
    productos = Producto.objects.all().values()
    context = {"productos": productos}
    
    return render(request, 'ropa/index.html', context)

def quienessomos(request):
    return render(request, 'ropa/quienessomos.html')


def productosAdd(request):
    context ={}
    
    if request.method == "POST":
        opcion = request.POST["opcion"]
        print(opcion)
        
        if opcion == "Añadir Producto":
            print("Opcion: "+opcion)
            try:
                sku = request.POST["sku"]
                try:
                    foto = request.FILES["fotop"]
                except:
                    foto = 'productos/fotodefault.png'
                nombre= request.POST["nombrep"]
                marca = request.POST["marcap"]
                cantidad = int(request.POST["cantidadp"])
                precio = int(request.POST["preciop"])
                descripcion = request.POST["descripcionp"]
                detalles = request.POST["detallesp"]
            
                print(sku, nombre, marca, cantidad, precio, descripcion, detalles)

                producto = Producto.objects.create(sku=sku, foto=foto, nombre=nombre, marca=marca, cantidad=cantidad, precio=precio, descripcion=descripcion, detalles=detalles)
                
                producto.save()
                context={'ac':'El producto ha sido agregado correctamente'}
                return render(request, 'ropa/productosAdd.html', context)
            except:
                context={'ac2':'No se pudo agregar el producto SKU(id) ya existe'}
                return render(request, 'ropa/productosAdd.html', context)
        
        if opcion == "Editar":
            
            productos = Producto.objects.all().values()
            context = {"productos": productos}
            return render(request, 'ropa/productosList.html', context)
        
        if opcion == "Actualizar":
            print("Entró a actualizar")
            print("Opción="+opcion)
            sku = request.POST["sku"]
            try:
                foto = request.FILES["fotop"]
            except:
                foto = 'productos/fotodefault.png'
            nombre= request.POST["nombrep"]
            marca = request.POST["marcap"]
            cantidad = int(request.POST["cantidadp"])
            precio = int(request.POST["preciop"])
            descripcion = request.POST["descripcionp"]
            detalles = request.POST["detallesp"]

            producto = Producto.objects.get(sku=sku)
            producto.sku=sku
            producto.foto=foto
            producto.nombre=nombre
            producto.marca=marca
            producto.cantidad=cantidad
            producto.precio=precio
            producto.descripcion=descripcion
            producto.detalles=detalles
            producto.save()

        
            productos = Producto.objects.all() 
            context={"productos": productos,"ac":"Bien, datos actualizados"}

            return render(request,'ropa/productosList.html',context)
        
    return render(request, 'ropa/productosAdd.html', context)

def productosEdit(request,pk):
    print("Hola estoy en productosEdit", pk)
    context={}
    producto = Producto.objects.get(sku=pk)
               
    context={"producto":producto}
    
    print("salió del for")
    return render(request,'ropa/productosEdit.html',context)

def productosDel(request, pk):
    print("Hola estoy en productosDel")
    try:
        producto = Producto.objects.get(sku=pk)
        nom= producto.nombre
        ruta_foto="media/"+str(producto.foto)
        producto.delete()
        if ruta_foto != "media/productos/fotodefault.png":
            import os
            os.remove(ruta_foto)

        productos = Producto.objects.all().values()
        context = {'ac':'Producto ('+str(nom)+') eliminado correctamente',"productos": productos}
        return render(request,'ropa/productosList.html', context)
    except:
        productos = Producto.objects.all()  
        context = {'ac':'No se pudo eliminar producto ('+str(nom)+')', "productos": productos}
        return render(request,'ropa/productosList.html', context)
    
def detalles(request, pk):
    print("Hola estoy en detalles producto", pk)
    context={}

    producto = Producto.objects.get(sku=pk)
    
    context={"producto":producto}
    
    print("salió del for")
    return render(request,'ropa/detalleproducto.html',context)

@login_required(login_url="login")
def carro(request):
     
    context={"carro":carro}
    
    return render(request, "ropa/carro.html",context)

def ver_pedidos(request):
    # pedidos = LineaPedido.objects.all().values()
    # print(LineaPedido)
    # context = {"pedidos":pedidos}
    # return render(request, 'ropa/verpedidos.html',context)
    
    pedidos = Pedido.objects.all()
    lineas_pedidos = LineaPedido.objects.filter(pedido__in=pedidos)
    context = {"pedidos": pedidos, "lineas_pedidos": lineas_pedidos}
    return render(request, 'ropa/verpedidos.html', context)
