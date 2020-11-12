from django.shortcuts import render, redirect
from .forms import  UserUpdateForm


def inicio(request):
    return render(request, "Principal/index.html")


def estacionamientos(request):
    return render(request, "Principal/estacionamientos.html")


def recorridos(request):
    return render(request, "Principal/recorridos.html")

