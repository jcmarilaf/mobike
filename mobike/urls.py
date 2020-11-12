from django.contrib import admin
from django.urls import path, include, re_path
from operator import index
from . import views
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', include('apps.Registro.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    path('', views.inicio, name="inicio"),
    path('estacionamientos', views.estacionamientos, name="estacionamientos"),
    path('ingresar/', auth_views.LoginView.as_view(template_name='Usuario/ingresar.html'), name='ingresar'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='cerrarSesion'),
    
    
    
    
    
    path('recuperarcontrasena/', PasswordResetView.as_view(template_name = 'Usuario/recuperarcontrasena.html'), name='recuperarcontrasena'),
    
    
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='Usuario/password_reset_done.html'), name='password_reset_done'),
    
    
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name=  'Usuario/password_reset_confirm.html') 
            , name='password_reset_confirm' ),
    
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='Usuario/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)