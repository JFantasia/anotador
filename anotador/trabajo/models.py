from datetime import datetime

from django.db import models
from parametros.models import Etiqueta, TipoIntervecion, Institucion
from persona.models import Persona
from parametros_trabajo.models import Actividad, UnidadProductiva, Programa, Trabajo
# Create your models here.


class Ficha(models.Model):
    ''' Modelo para representar los empleos gestionados por la organización '''
    estado_programa = [
        ('a', 'Activo'),
        ('i', 'Inactivo'),
    ]
    estado_persona = [
        ('t', 'Trabaja'),
        ('n', 'No Trabaja'),
    ]
    persona = models.ForeignKey(Persona, models.CASCADE, related_name= "tfp")
    actividad = models.ForeignKey(Actividad, models.CASCADE)
    unidad_productiva = models.ForeignKey(UnidadProductiva, models.CASCADE)
    programa = models.ForeignKey(Programa, models.CASCADE)
    trabajo = models.ForeignKey(Trabajo, models.CASCADE)
    horas = models.IntegerField()
    estado_programa = models.CharField(max_length=10, choices=estado_programa)
    estado_persona = models.CharField(max_length=10, choices=estado_persona)
    ingreso = models.DateField(default=datetime.now)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Fichas"

class Intervencion(models.Model):
    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE, related_name="tti", limit_choices_to={'app__nombre': 'Trabajo'})
    institucion = models.ForeignKey(Institucion, models.CASCADE, related_name="ttin")
    persona = models.ForeignKey(Ficha, models.CASCADE)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Intervenciones"

class Lista_Espera(models.Model):
    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    fecha = models.DateField()
    actividad = models.ForeignKey(Actividad, models.CASCADE, related_name="ale")
    persona = models.ForeignKey(Persona, models.CASCADE)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Lista de Espera"

class Nota(models.Model):
    ''' Modelo para representar las notas de trabajo '''
    fecha = models.DateField()
    etiqueta = models.ForeignKey(Etiqueta, models.CASCADE, related_name= "net", null=True, blank=True)
    resumen = models.CharField(max_length=50)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.resumen}"

    class Meta:
        verbose_name_plural = "Notas"
