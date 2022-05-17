from django.db import models

# Create your models here.

class Deposito(models.Model):
    ''' Modelo para representar los depósitos de mercaderías '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Depósitos"

class UnidadMedida(models.Model):
    ''' Modelo para representar las unidades de medida de los productos '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Unidades de Medida"

