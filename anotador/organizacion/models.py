from datetime import datetime

from django.db import models

# Create your models here.
from persona.models import Persona
from parametros.models import Etiqueta, Ciudad, Institucion
from persona.models import Grupo

class Organizacion(models.Model):
    ''' Modelo para representar las fichas de las organizaciones '''
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Organizaciones"

class TipoEspacio(models.Model):
    ''' Modelo para representar los tipos de espacios físicos '''
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipo de Espacio Físico"

class Espacio(models.Model):
    ''' Modelo para representar los espacios físicos '''
    nombre = models.CharField(max_length=100)
    organizacion = models.ForeignKey(Organizacion, models.CASCADE)
    tipo = models.ForeignKey(TipoEspacio, models.CASCADE)
    direccion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, models.CASCADE)
    responsable = models.ForeignKey(Persona, models.CASCADE, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} - {self.organizacion}"

    class Meta:
        verbose_name_plural = "Espacios Físicos"

class Recurso(models.Model):
    ''' Modelo para representar los recursos de las organizaciones '''
    identificacion = models.CharField(max_length=50, unique=True)
    adquisicion = models.DateField()
    etiqueta = models.ForeignKey(Etiqueta, models.CASCADE, related_name= "etreq")
    espacio = models.ForeignKey(Espacio, models.CASCADE)
    responsable = models.ForeignKey(Persona, models.CASCADE, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.identificacion} - {self.etiqueta}"

    class Meta:
        verbose_name_plural = "Recursos"

class Reserva(models.Model):
    ''' Modelo para representar las reservas de uso de recursos '''
    fecha = models.DateField()
    recursos = models.ManyToManyField(Recurso, related_name="recRes")
    solicitantes = models.ForeignKey(Grupo, models.CASCADE)
    responsable = models.ForeignKey(Persona, models.CASCADE, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.solicitantes} - {self.recursos}"

    class Meta:
        verbose_name_plural = "Reservas"

class TipoTarea(models.Model):
    ''' Modelo para representar los tipos de tareas '''
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Tareas"

class Tarea(models.Model):
    ''' Modelo para representar las tareas planificadas '''
    estados = [
    ('P','Pendiente'),
    ('F','Finalizada'),
    ('C','Cancelada'),
    ]
    organizacion = models.ForeignKey(Organizacion, models.CASCADE)
    tipo = models.ForeignKey(TipoTarea, models.CASCADE)
    nombre = models.CharField(max_length=100)
    planificacion = models.DateField()
    limite = models.DateField(blank=True, null=True)
    responsable = models.ForeignKey(Persona, models.CASCADE, blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.CASCADE, blank=True, null=True)
    relaciones = models.ManyToManyField(Institucion)
    detalle = models.TextField(blank=True, null=True)
    estado = models.CharField('Estado', max_length=1, choices=estados, default='P')


    def __str__(self):
        return f"{self.nombre} - {self.organizacion} - {self.limite}"

    class Meta:
        verbose_name_plural = "Tareas"
