from django.contrib import admin
from .models import Post, Cliente, Pedido, Categoria

# Register your models here.

admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Categoria)