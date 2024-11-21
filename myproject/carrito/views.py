from django.shortcuts import render,redirect,get_object_or_404
from productos.models import Producto
from carrito.models import Carrito, ItemCarrito

# Create your views here.
def carrito(request,total=0,cantidad=0,items_carrito=None):
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        items_carrito = ItemCarrito.objects.filter(carrito=carrito,activo=True)
        for item_carrito in items_carrito:
            total += (item_carrito.producto.precio * item_carrito.cantidad)
            cantidad += item_carrito.cantidad
        gran_total = total
    except ObjectNotExist:
        pass
    context ={
        'total': total,
        'cantidad': cantidad,
        'items_carrito': items_carrito,
        'gran_total': gran_total,
    }
    return render(request,'carrito.html',context)

def añadir_carrito(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request)) # toma el carrito usando el carrito_id presente en la sesion
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            carrito_id = _carrito_id(request)
        )
    carrito.save()

    try:
        carrito_item = ItemCarrito.objects.get(producto=producto,carrito=carrito)
        carrito_item.cantidad += 1
        carrito_item.save()
    except ItemCarrito.DoesNotExist:
        carrito_item = ItemCarrito.objects.create(
            producto = producto,
            cantidad = 1,
            carrito = carrito,
        )
        carrito_item.save()
    return redirect('carrito')
def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def remover_carrito(request,producto_id):
    carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    producto = get_object_or_404(Producto,id=producto_id)
    item_carrito = ItemCarrito.objects.get(producto=producto, carrito=carrito)
    if item_carrito.cantidad > 1:
        item_carrito.cantidad -= 1
        item_carrito.save()
    else:
        item_carrito.delete()
    return redirect('carrito')