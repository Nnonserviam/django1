from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('about/', views.about, name='about'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('contacto/', views.contacto, name='contacto'),
]