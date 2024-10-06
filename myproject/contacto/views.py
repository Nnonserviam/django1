from django.shortcuts import render,redirect
from .forms import MensajeContactoForm
from django.contrib import messages
from django.core.mail import send_mail

def contacto(request):
    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            # Enviar correo electrónico
            send_mail(
                f"Nuevo mensaje de contacto: {mensaje.asunto}",
                f"Nombre: {mensaje.nombre}\nEmail: {mensaje.email}\nMensaje: {mensaje.mensaje}",
                'emailpruebabackend@gmail.com',  
                ['camilo.ibanez.95@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect('mensaje_enviado')
        else:
            messages.error(request, "Error al enviar el mensaje. Por favor, revisa los campos.")
    else:
        form = MensajeContactoForm()
    return render(request, 'contacto.html', {'form': form})