from datetime import datetime

from django.db import models

# Create your models here.
from parametros.models import Localidad, Nacionalidad


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
    documento = models.CharField(max_length=8, unique=True)
    cuit = models.CharField(max_length=11, unique=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    piso_dpto = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=20, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, models.CASCADE, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(default=datetime.now)
    ingreso = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.CASCADE)

    def __str__(self):
        return f"{self.documento} - {self.apellido}, {self.nombre}"

    class Meta:
        verbose_name_plural = "Personas"
