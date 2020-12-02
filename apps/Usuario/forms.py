from .models import Usuario
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'last_name',
            'email':'Correo',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'picture'
        ]
