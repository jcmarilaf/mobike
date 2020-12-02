from django.shortcuts import render, redirect
from .models import Recorridos, Post
from .forms import RecorridosForm,PostForm
from django.db.models import Q
from apps.Usuario.models import Usuario
from django.views.generic import ListView
from apps.Usuario.forms import UserUpdateForm
from django.contrib import messages
#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

#-----------------------APPI----------------------------

def api_tarjeta(request):
    return render(request, "Principal/tarjeta.html")


def listar_recorridos(request):
    recorridos = Recorridos.objects.all().filter(usuario=request.user)

    return render(request, "Principal/recorridos.html", {'recorridos': recorridos})

def agregar_recorridos(request):
    if request.method == "POST":
        form = RecorridosForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("agregar_recorridos")
    else:
        form = RecorridosForm()
        return render(request, "Registro/agregar_recorridos.html", {'form': form})


def borrar_recorridos(request, recorridos_id):
    # Recuperamos la instancia de la bicicleta y la borramos
    instancia = Recorridos.objects.get(id=recorridos_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_recorridos')


def editar_recorridos(request, recorridos_id):
    # Recuperamos la instancia de la carrera
    instancia = Recorridos.objects.get(id=recorridos_id)

    # Creamos el formulario con los datos de la instancia
    form = RecorridosForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = RecorridosForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_recorridos.html", {'form': form})





# VENTANA POST

def listar_post(request):
    post = Post.objects.all()
    return render(request, "Registro/post.html", {'post': post})

def agregar_post(request):
    if request.method == "POST":
        form = PostForm( request.POST , request.FILES, request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            messages.success(request,'¡Su post ha sido creado!')
            return redirect("listar_post")
        else:
            messages.error(request, "Error, No se pudo subir su post")
    else:
        form = PostForm()
        return render(request, "Registro/agregar_post.html", {'form': form})

def borrar_post(request, post_id):
    # Recuperamos la instancia de la bicicleta y la borramos
    instancia = Post.objects.get(id=post_id)
    instancia.delete()
    messages.success(request,'¡Post eliminado correctamente!')
    # Después redireccionamos de nuevo a la lista
    return redirect('listar_post')

def editar_post(request,post_id):
    
    # Recuperamos la instancia de la carrera
    instancia = Post.objects.get(id=post_id)
    
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = PostForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            form.save()
            messages.success(request,'¡Post editado correctamente!')
            return redirect('listar_post')
        else:
            messages.error(request, "Error, No se pudo editar su post")
    else:
        form = PostForm(instance=instancia)

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_post.html", {'form': form})



@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
 
@api_view(['GET'])
def post_element(request, pk):
    post = get_object_or_404(Post, id=pk)
 
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_collection(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_element(request, pk):
    post = get_object_or_404(Post, id=pk)
 
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        post_new = JSONParser().parse(request) 
        serializer = PostSerializer(post, data=post_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
