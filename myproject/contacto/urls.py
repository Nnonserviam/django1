from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    path('mensaje_enviado/',TemplateView.as_view(template_name='mensaje_enviado.html'),name='mensaje_enviado'),
]


