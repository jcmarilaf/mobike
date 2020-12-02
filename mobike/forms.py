from apps.Usuario.models import Usuario
from django import forms
from django.contrib.auth.forms import UserCreationForm

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
