from django.contrib import admin
from django.urls import path,include
from . import views
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', views.productos, name='productos'),
    path('about/', views.about, name='about'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
]