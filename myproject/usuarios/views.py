from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
def ingresar(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige a los usuarios ya autenticados
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:   
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def registrar(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige a los usuarios ya autenticados
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Cuenta creada exitosamente para {username}')
            return redirect('home')
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores.')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'form': form})