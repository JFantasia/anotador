from django.db import models

# Create your models here.
from parametros.models import Ciudad


class Grupo(models.Model):
    ''' Modelo para representar las personas en la plataforma '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Grupos"

class Persona(models.Model):
    ''' Modelo para representar las personas en la plataforma '''
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    documento = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, models.CASCADE)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    ingreso = models.DateField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.CASCADE)

    def __str__(self):
        return f"{self.documento} - {self.apellido}, {self.nombre}"

    class Meta:
        verbose_name_plural = "Personas"
