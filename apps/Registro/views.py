from django.shortcuts import render, redirect
from .models import Recorridos
from .forms import RecorridosForm

# Create your views here.

def listar_recorridos(request):
    recorridos = Recorridos.objects.all()
    return render(request, "Registro/listar_recorridos.html", {'recorridos': recorridos})

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

