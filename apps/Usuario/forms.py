from .models import Usuario
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'nombres',
            'apellido',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'nombres':'Nombre',
            'apellido':'Apellido',
            'email':'Correo',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = [
            'username',
            'nombres',
            'apellido',
            'email',
            'imagen'
        ]
