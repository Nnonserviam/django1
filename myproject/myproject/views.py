from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from productos.models import Producto # Añade esta línea


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def testimonios(request):
    return render(request, 'testimonios.html')

def contacto(request):
    return render(request, 'contacto.html')


