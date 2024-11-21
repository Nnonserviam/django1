from django.shortcuts import render, get_object_or_404
from .carrito import Carrito
from productos.models import Producto
from django.http import JsonResponse



def ver_carrito(request):
    return render(request, 'carrito.html',{})

def agregar_al_carrito(request, producto_id):
    carrito = Carrito(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto_id'))
        producto = get_object_or_404(Producto, id=producto_id)
        #guardar en la sesion
        carrito.agregar(producto=producto)
        #retornar respuesta
        respuesta = JsonResponse({'Nombre Producto: ': producto.nombre})
        return respuesta

def eliminar_del_carrito(request, producto_id):
    return render(request, 'carrito.html')

def actualizar_carrito(request, producto_id, cantidad):
    return render(request, 'carrito.html')

