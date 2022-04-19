from django.db import models

# Create your models here.

class Pais(models.Model):
    ''' Modelo para representar paises '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    ''' Modelo para representar provincias '''
    nombre = models.CharField(max_length=200, unique=True)
    pais = models.ForeignKey(Pais, models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.pais}"

    class Meta:
        verbose_name_plural = "Provincias"


class Ciudad(models.Model):
    ''' Modelo para representar ciudades '''
    nombre = models.CharField(max_length=200, unique=True)
    provincia = models.ForeignKey(Provincia, models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.provincia}"

    class Meta:
        verbose_name_plural = "Ciudades"

class Aplicacion(models.Model):
    ''' Modelo para representar las aplicaciones '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Aplicaciones"

class Sexo(models.Model):
    ''' Modelo para representar las aplicaciones '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Sexos"

class Genero(models.Model):
    ''' Modelo para representar las aplicaciones '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Generos"

class TipoIntervecion(models.Model):
    ''' Modelo para representar los tipos de intervenciones segmentado por aplicación '''
    tipo = models.CharField(max_length=200)
    app = models.ForeignKey(Aplicacion, models.CASCADE)

    def __str__(self):
        return f"{self.tipo}, {self.app}"

    class Meta:
        verbose_name_plural = "Tipos de Intervenciones"