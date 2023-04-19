from django.db import models

# Create your models here.

class Cobertura(models.Model):
    ''' Modelo para representar las Coberturas Médicas '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Coberturas Médicas"

class Enfermedad(models.Model):
    ''' Modelo para representar las enfermedades '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Enfermedades"

class EnfermedadCronica(models.Model):
    ''' Modelo para representar las enfermedades '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Enfermedades Crónicas"

class Dificultad(models.Model):
    ''' Modelo para representar las dificultades '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Dificultades"

class ElementoCuidado(models.Model):
    ''' Modelo para representar los Elementos de Cuidado '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Elementos de Cuidado"

class ProblematicaBarrio(models.Model):
    ''' Modelo para representar las Problemáticas del Barrio '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Problemáticas del Barrio"

class PresionArterial(models.Model):
    ''' Modelo para representar las Presiones Arteriales '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Presiones Arteriales"

class IdentificaColores(models.Model):
    ''' Modelo para representar los opciones del desplegable identifica colores '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Opciones desplegable identifica colores"

class VeNumerosLetras(models.Model):
    ''' Modelo para representar los opciones del desplegable ve números y letras '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Opciones desplegable ve números y letras"

class TestVistaCerca(models.Model):
    ''' Modelo para representar los opciones del desplegable ve números y letras '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Opciones test vista cerca"

class TestVistaLejos(models.Model):
    ''' Modelo para representar los opciones del desplegable ve números y letras '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Opciones test vista lejos"

class Autopercepcion(models.Model):
    ''' Modelo para representar los opciones del desplegable ve números y letras '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Opciones de Autopercepción"

class Medicamento(models.Model):
    ''' Modelo para representar los medicamentos entregados/recetados en las atenciones de salud '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Medicamentos"

class SituacionVivienda(models.Model):
    ''' Modelo para representar las situaciones habitacionales '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Situaciones de las Viviendas"

class MaterialVivienda(models.Model):
    ''' Modelo para representar las situaciones habitacionales '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Materiales de las Viviendas"

class ServicioVivienda(models.Model):
    ''' Modelo para representar las situaciones habitacionales '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicios de las Viviendas"

class Especialidad(models.Model):
    ''' Modelo para representar las especialidades de profesionales de la salud '''
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Especialidades"