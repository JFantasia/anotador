from datetime import datetime

from django.db import models

# Create your models here.
from persona.models import Persona
from parametros.models import Genero, Institucion, TipoIntervecion

class Ficha(models.Model):
    ''' Modelo para representar las fichas de géneros de las personas en la plataforma '''
    persona = models.ForeignKey(Persona, models.CASCADE, related_name= "gfp")
    genero = models.ForeignKey(Genero, models.CASCADE)
    situacion_violencia = models.BooleanField(default=False)
    situacion_habitacional = models.BooleanField(default=False)
    situacion_familiar = models.BooleanField(default=False)
    situacion_justicia = models.BooleanField(default=False)
    situacion_salud = models.BooleanField(default=False)
    situacion_consumo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.persona}"

    class Meta:
        verbose_name_plural = "Fichas"


class Intervencion(models.Model):
    ''' Modelo para representar las Intervenciones de géneros de las personas en la plataforma '''
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE, related_name="gti", limit_choices_to={'app__nombre': 'Géneros'})
    institucion = models.ForeignKey(Institucion, models.CASCADE, related_name="gtin")
    persona = models.ForeignKey(Ficha, models.CASCADE)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Intervenciones"

