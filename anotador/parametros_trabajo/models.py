from django.db import models
from parametros.models import Localidad

# Create your models here.

class UnidadProductiva(models.Model):
    ''' Modelo para representar las unidades productivas de la organiozación '''

    nombre = models.CharField(max_length=200)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    piso_dpto = models.CharField(max_length=20)
    cp = models.CharField(max_length=20)
    localidad = models.ForeignKey(Localidad, models.CASCADE)
    inicio_actividades = models.DateField(blank=True)
    registro = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Unidades Productivas"

class Dependencia(models.Model):
    ''' Modelo para representar las dependencias del estado '''

    nombre = models.CharField(max_length=200)
    local =  models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Dependencias"

class Programa(models.Model):
    ''' Modelo para representar los programas del estado '''

    nombre = models.CharField(max_length=200)
    dependencia = models.ForeignKey(Dependencia, models.CASCADE)


    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Programas"

class Trabajo(models.Model):
    ''' Modelo para representar los tipos de trabajos a realizar '''

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Trabajos"

class Rama(models.Model):
    ''' Modelo para representar las ramas de actividades de trabajos '''

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Ramas"

class Actividad(models.Model):
    ''' Modelo para representar los tipos de trabajos a realizar '''

    nombre = models.CharField(max_length=200)
    rama = models.ForeignKey(Rama, models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Actividades"
