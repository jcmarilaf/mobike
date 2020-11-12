from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList, Usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    path('perfil', views.Usuario , name='perfil'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
