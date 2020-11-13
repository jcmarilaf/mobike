from django import forms
from .models import Bicicleta, Recorridos, Post

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['marca', 'aro', 'codigo']

        labels = {
            'marca': 'Marca',
            'aro': 'Aro',
            'codigo': 'Codigo',
        }
        
class RecorridosForm(forms.ModelForm):
    class Meta:
        model = Recorridos
        fields = ['usuario','bicicleta','kilometros_total','origen','destino','valor_total']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['usuario','titulo','descripcion','imagen']

