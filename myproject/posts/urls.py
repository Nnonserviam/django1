from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('home', views.home, name='homep'),
    path('productos.html',views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name='page')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)