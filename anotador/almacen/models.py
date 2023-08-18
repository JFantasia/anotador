from django.db import models
from parametros.models import Institucion

from persona.models import Grupo, Persona

# Create your models here.

class TipoArticulo(models.Model):
    ''' Modelo para representar los tipos de artículos'''

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Artículos"

class Articulo(models.Model):
    ''' Modelo para representar los artículos'''

    nombre = models.CharField(max_length=200)
    tipoArticulo = models.ForeignKey(TipoArticulo, models.CASCADE)
    esAlimento = models.BooleanField(default=False)
    esRopa = models.BooleanField(default=False)
    esMaterial = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Artículos"

class Entrega(models.Model):
    ''' Modelo para representar la entrega de articulos '''
    estados = [
    ('P','Pendiente'),
    ('C','Procesada'),
    ]
    fecha = models.DateField(verbose_name='Fecha de Entrega')
    referencia = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, models.CASCADE, related_name="fk_alm_per", blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.CASCADE, related_name="fk_alm_gr", blank=True, null=True)
    estado = models.CharField('Estado', max_length=1, choices=estados, default='P')

    def __str__(self):
        return f"{self.fecha} - {self.persona} - {self.grupo}"

    class Meta:
        verbose_name_plural = "Entregas de Artículos"

class DetalleEntrega(models.Model):
    ''' Modelo para representar los items de la entrega de los artículos '''
    entrega = models.ForeignKey(Entrega, models.CASCADE, related_name="fk_det_ent")
    articulo = models.ForeignKey(Articulo, models.CASCADE, related_name="fk_det_ent_art")
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.articulo} - {self.cantidad}"

    class Meta:
        verbose_name_plural = "Detalle de Entregas de Artículos"

class Recepcion(models.Model):
    ''' Modelo para representar la recepcion de articulos '''
    estados = [
    ('P','Pendiente'),
    ('C','Procesada'),
    ]
    fecha = models.DateField(verbose_name='Fecha de Entrega')
    referencia = models.CharField(max_length=100)
    institucion = models.ForeignKey(Institucion, models.CASCADE, related_name="fk_rec_alm_inst", blank=True, null=True)
    persona = models.ForeignKey(Persona, models.CASCADE, related_name="fk_rec_alm_per", blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.CASCADE, related_name="fk_rec_alm_gr", blank=True, null=True)
    esComprado = models.BooleanField(default=False, verbose_name="Es Comprado")
    estado = models.CharField('Estado', max_length=1, choices=estados, default='P')
    
    def __str__(self):
        return f"{self.fecha} - {self.esComprado}"

    class Meta:
        verbose_name_plural = "Recepcion de Artículos"

class DetalleRecepcion(models.Model):
    ''' Modelo para representar los items de la recepcion de los artículos '''
    recepcion = models.ForeignKey(Recepcion, models.CASCADE, related_name="fk_det_rec")
    articulo = models.ForeignKey(Articulo, models.CASCADE, related_name="fk_det_rec_art")
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.articulo} - {self.cantidad}"

    class Meta:
        verbose_name_plural = "Detalle de Recepcion de Artículos"
