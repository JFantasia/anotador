from django.db import models

# Create your models here.

class Pais(models.Model):
    ''' Modelo para representar paises '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Paises"

class Nacionalidad(models.Model):
    ''' Modelo para representar nacionalidad '''
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Nacionalidades"

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

class Localidad(models.Model):
    ''' Modelo para representar localidades de una ciudad '''
    nombre = models.CharField(max_length=200, unique=True)
    ciudad = models.ForeignKey(Ciudad, models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.ciudad}"

    class Meta:
        verbose_name_plural = "Localidades"

class Aplicacion(models.Model):
    ''' Modelo para representar las aplicaciones '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Aplicaciones"

class Genero(models.Model):
    ''' Modelo para representar las Generos '''
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

class Institucion(models.Model):
    ''' Modelo para representar las Instituciones relacionadas a intervenciones '''
    nombre = models.CharField(max_length=200)
    esEducativa = models.BooleanField(default=False)
    esCentroFormacion = models.BooleanField(default=False)
    esCuidados = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Instituciones"

class Etiqueta(models.Model):
    ''' Modelo para representar etiquetas para notas '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Etiquetas"