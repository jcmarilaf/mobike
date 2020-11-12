from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # listar las bicicleta de la bd
    path('recorridos', views.listar_recorridos, name="recorridos"),
    
    # agregar una bicicleta    
    path('agregar_recorridos', views.agregar_recorridos, name="agregar_recorridos"),
    
        # editar una bicicleta
    path('editar_recorridos/<int:recorridos_id>', views.editar_recorridos ,name="editar_recorridos"),

    # borrar una bicicleta
    path('borrar_recorridos/<int:recorridos_id>', views.borrar_recorridos, name="borrar_recorridos"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)