from django import forms
from .models import Bicicleta, Recorridos

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
        model : Recorridos
        fields = ['usuario','bicicleta','kilometros_total','origen','destino','valor_total','fecha_registro']
