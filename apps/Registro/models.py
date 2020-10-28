from django.db import models

# Create your models here.
class Bicicleta(models.Model):
    marca = models.CharField(max_length=30)
    aro = models.IntegerField()
    codigo = models.IntegerField()

    def __str__(self):
        return self.marca

class Cliente(models.Model):
    Bicicleta = models.ForeignKey(Bicicleta, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno
