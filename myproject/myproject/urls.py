from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('', include('productos.urls')),
    path('', include('contacto.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('testimonios/', views.testimonios, name='testimonios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

