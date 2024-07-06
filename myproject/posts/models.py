from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def str(self):
        return self.nombre

class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='luffy.png', blank=True)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categorias')

    def str(self):
        return self.nombre


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=20)
    apellido = models.CharField(max_length=20)
    infoContacto = models.TextField()
    detFacturacion = models.IntegerField()
    histCompras = models.IntegerField()

    def str(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGADO', 'Entregado'),
    ]

    idpedido = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='productos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clientes')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    fechaPedido = models.DateTimeField(default=timezone.now)
    fechaEntrega = models.DateTimeField(null=True, blank=True)
    def str(self):
        return self.nombre

