from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error en el registro.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrar.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')