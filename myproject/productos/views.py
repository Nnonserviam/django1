from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Producto



def productos(request):
    productos = Producto.objects.all()
    template = loader.get_template('productos.html')
    context = {
        'productos': productos,
    }
    return HttpResponse(template.render(context, request))
def detalle(request,id):
    producto = Producto.objects.get(id=id)
    template = loader.get_template('detalle.html')
    context = {
        'producto': producto,
    }
    return HttpResponse(template.render(context, request))
