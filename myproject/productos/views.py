from django.shortcuts import render
from productos.models import Producto

# ... otras importaciones y vistas ...

def productos(request):
    lista_productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': lista_productos})

# ... resto del código ...