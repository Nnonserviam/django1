from django.db import models
from productos.models import Producto

# Create your models here.
class Carrito(models.Model):
    carrito_id = models.CharField(max_length=250, blank=True)
    fecha_añadido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def sub_total(self):
        return self.producto.precio * self.cantidad
    def __str__(self):
        return self.producto