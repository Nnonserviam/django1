from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registrar/',views.registrar_view, name="registrar"),
    path('ingresar/',views.ingresar_view, name="ingresar"),
    path('salir/', views.salir_view, name="salir"),
]

