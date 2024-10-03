from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Producto

# ... otras importaciones y vistas ...

def productos(request):
    productos = Producto.objects.all()
    template = loader.get_template('productos.html')
    context = {
        'productos': productos,
    }
    return HttpResponse(template.render(context, request))
# ... resto del código ...