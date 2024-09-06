from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('ingresar/', views.ingresar, name='ingresar'),
    path('registrar/', views.registrar, name='registrar'),
    

    # ... otras URLs de usuarios ...
]