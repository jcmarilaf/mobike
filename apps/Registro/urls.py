from django.urls import path, include
from . import views

urlpatterns = [

    # listar las bicicleta de la bd
    path('listar_recorridos', views.listar_recorridos, name="listar_recorridos"),
    
    # agregar una bicicleta    
    path('agregar_recorridos', views.agregar_recorridos, name="agregar_recorridos"),
    
        # editar una bicicleta
    path('editar_recorridos/<int:recorridos_id>', views.editar_recorridos ,name="editar_recorridos"),

    # borrar una bicicleta
    path('borrar_recorridos/<int:recorridos_id>', views.borrar_recorridos, name="borrar_recorridos"),

]