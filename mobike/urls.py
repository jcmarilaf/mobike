from django.contrib import admin
from django.urls import path, include
from operator import index
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('apps.Registro.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    path('', views.inicio, name="inicio"),
    path('estacionamientos', views.estacionamientos, name="estacionamientos"),
    path('recorridos', views.recorridos, name="recorridos"),
    path('ingresar/', auth_views.LoginView.as_view(template_name='Usuario/ingresar.html'), name='ingresar'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='cerrarSesion'),
]
