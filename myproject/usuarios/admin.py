from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'email')
    ordering = ('nombre', 'apellido_paterno', 'apellido_materno', 'email')

admin.site.register(Usuario, CustomUserAdmin)