from django.shortcuts import render, redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from .models import Usuario


# Create your views here.

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('ingresar')
 
 
class UserList(ListView):
    model = Usuario
    template_name = 'Usuario/list_user.html'