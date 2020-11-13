from django.shortcuts import render, redirect
from .models import Recorridos, Post
from .forms import RecorridosForm,PostForm
from django.db.models import Q
from apps.Usuario.models import Usuario
from django.views.generic import ListView
from apps.Usuario.forms import UserUpdateForm
from django.contrib import messages


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
