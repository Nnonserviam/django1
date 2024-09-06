from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class CategoriaAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('gestionar-categorias/', self.admin_view(self.gestionar_categorias), name='gestionar_categorias'),
        ]
        return custom_urls + urls

    def gestionar_categorias(self, request):
        if request.method == 'POST':
            accion = request.POST.get('accion')
            if accion == 'agregar':
                nombre = request.POST.get('nombre')
                Categoria.objects.create(nombre=nombre)
                messages.success(request, f'Categoría "{nombre}" agregada con éxito.')
            elif accion == 'eliminar':
                categoria_id = request.POST.get('categoria_id')
                Categoria.objects.filter(id=categoria_id).delete()
                messages.success(request, 'Categoría eliminada con éxito.')
            return redirect('admin:gestionar_categorias')

        categorias = Categoria.objects.all()
        return render(request, 'admin/gestionar_categorias.html', {'categorias': categorias})

admin_site = CategoriaAdminSite(name='myadmin')
admin_site.register(Producto, ProductoAdmin)
admin_site.register(Categoria, CategoriaAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

# Reemplaza el admin site por defecto
admin.site = admin_site
admin.sites.site = admin_site