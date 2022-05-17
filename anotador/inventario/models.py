from django.db import models

# Create your models here.
from parametros_inventario import UnidadMedida ,Deposito



class Proveedor(models.Model):
    ''' Modelo para representar los proveedores de mercaderías '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Proveedores"

class Producto(models.Model):
    ''' Modelo para representar los productos '''
    nombre = models.CharField(max_length=200)
    unidad_medida = models.ForeignKey(UnidadMedida, models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Productos"

class InventarioProducto(models.Model):
    ''' Modelo para representar los productos en stock en un depósito '''
    deposito = models.ForeignKey(Deposito, models.CASCADE)
    producto = models.ForeignKey(Producto, models.CASCADE)
    cantidad = models.FloatField(default=0)

    def __str__(self):
        return f"{self.deposito} - {self.producto}: {self.cantidad}"

    class Meta:
        verbose_name_plural = "Inventario de Productos"

class Movimiento(models.Model):
    ''' Modelo para representar los productos en stock en un depósito '''
    deposito_origen = models.ForeignKey(Deposito, models.CASCADE, related_name="movorig")
    deposito_destino = models.ForeignKey(Deposito, models.CASCADE, related_name="movdest")
    cantidad = models.FloatField(default=0)

    def __str__(self):
        return f"{self.deposito_origen} - {self.deposito_destino}: {self.cantidad}"

    class Meta:
        verbose_name_plural = "Movimientos entre depósitos"