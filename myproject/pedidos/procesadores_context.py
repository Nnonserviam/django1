from .carrito import Carrito

#crear procesador de contexto para que el carrito este disponible en todas las vistas
def carrito(request):
    #retornar default data del carrito
    return {'carrito': Carrito(request)}
