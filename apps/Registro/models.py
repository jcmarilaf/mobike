from django.db import models
from apps.Usuario.models import Usuario

# Create your models here.
class Bicicleta(models.Model):
    codigo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)
    aro = models.IntegerField()
    def __str__(self):
        return  str(self.codigo)
    
class Recorridos(models.Model):
    usuario = models.ForeignKey(Usuario,null=False, on_delete=models.CASCADE)
    bicicleta = models.ForeignKey(Bicicleta, null=False, on_delete=models.CASCADE)
    kilometros_total = models.DecimalField(default=0,max_digits=3 ,decimal_places = 2)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    valor_total = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.origen + '-' + self.destino

class Post (models.Model):
    usuario = models.ForeignKey(Usuario,null=False, on_delete=models.CASCADE)
    titulo = models.CharField( max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_post = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(
        'Imagen de perfil', upload_to='post/', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.titulo