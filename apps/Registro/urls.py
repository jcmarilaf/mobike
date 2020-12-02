from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # listar las recorridos de la bd
    path('recorridos', views.listar_recorridos, name="recorridos"),
    
    # listar post
    path('post', views.listar_post, name="listar_post"),
    
    # agregar una post   
    path('agregar_post', views.agregar_post, name="agregar_post"),
    
    # editar una post
    path('editar_post/<int:post_id>', views.editar_post ,name="editar_post"),

    # borrar una post
    path('borrar_post/<int:post_id>', views.borrar_post, name="borrar_post"),
    
    path('tarjeta', views.api_tarjeta, name="tarjeta"),

      # api
    path('post_api/',  views.post_collection , name='post_collection'),
    path('post_api/<int:pk>/', views.post_element ,name='post_element')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)