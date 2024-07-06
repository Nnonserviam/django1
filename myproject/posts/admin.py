from django.contrib import admin
from .models import Post, Cliente, Pedido, Categoria

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('idpedido', 'estado', 'cliente','fechaPedido','fechaEntrega') 
    list_editable = ('estado',)
    list_filter = ('estado',)
    search_fields = ('idpedido', 'status', 'other_fields') 

admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Categoria)