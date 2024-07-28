from django.contrib import admin
from .models import Post, Cliente, Pedido, Categoria, PedidoProducto

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('idpedido', 'estado', 'cliente', 'fechaPedido', 'fechaEntrega')
    list_editable = ('estado',)
    list_filter = ('estado',)
    search_fields = ('idpedido', 'estado', 'cliente__nombre')
    inlines = [PedidoProductoInline]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass