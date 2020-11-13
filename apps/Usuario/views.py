from django.shortcuts import render, redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm, UserUpdateForm
from .models import Usuario
from django.contrib import messages


# Create your views here.

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('ingresar')
 

@login_required
def Usuario(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , request.FILES, instance= request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'¡Su perfil ha sido actualizado!')
            return redirect('perfil')
        else:
            messages.error(request, "Error, No se pudo realizar el cambio")
    else:
        u_form = UserUpdateForm(instance = request.user)
        
    context = {
        'u_from': u_form
    }
    
    return render(request,'Usuario/perfil.html', context)
