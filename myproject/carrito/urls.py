from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('añadir_carrito/<int:producto_id>/', views.añadir_carrito, name='añadir_carrito'),
    path('remover_carrito/<int:producto_id>/', views.remover_carrito, name='remover_carrito'),
]
