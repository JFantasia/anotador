from django.db import models

# Create your models here.
from persona.models import Persona
from parametros.models import Sexo, Genero, TipoIntervecion

class Ficha(models.Model):
    ''' Modelo para representar las fichas de salud de las personas en la plataforma '''
    persona = models.ForeignKey(Persona, models.CASCADE)
    sexo = models.ForeignKey(Sexo, models.CASCADE)
    genero = models.ForeignKey(Genero, models.CASCADE)
    ingreso = models.DateField()

    def __str__(self):
        return f"{self.persona}"

    class Meta:
        verbose_name_plural = "Fichas"

class Intervencion(models.Model):
    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE)
    persona = models.ForeignKey(Ficha, models.CASCADE)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Intervenciones"
