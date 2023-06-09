from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from parametros.models import Genero, Institucion, Nacionalidad


class Parentezco(models.Model):
    ''' Modelo para representar las relaciones de parentezco de les convivientes '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Parentezcos"

class EspaciosPoderosa(models.Model):
    ''' Modelo para representar los espacios de La Poderosa '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Espacios de la Poderosa"

class TipoTrabajo(models.Model):
    ''' Modelo para representar los tipos de trabajos '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Trabajos"

class OpcionesLuz(models.Model):
    ''' Modelo para representar la provisión de luz '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicio de Luz"

class OpcionesAgua(models.Model):
    ''' Modelo para representar la provisión de agua potable'''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicio de Agua Potable"

class OpcionesResiduos(models.Model):
    ''' Modelo para representar la recolección de residuos '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicio de Recolección de Residuos"

class OpcionesGas(models.Model):
    ''' Modelo para representar la provisión de gas'''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicio de Gas"

class OpcionesCloacas(models.Model):
    ''' Modelo para representar la provisión de cloacas'''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Servicio de Cloacas"

class TipoVivienda(models.Model):
    ''' Modelo para representar los tipos de viviendas '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Viviendas"

class MaterialesTecho(models.Model):
    ''' Modelo para representar los tipos de techos '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Materiales de Techos"

class MaterialesPared(models.Model):
    ''' Modelo para representar los tipos de paredes '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Materiales de Paredes"

class MaterialesPiso(models.Model):
    ''' Modelo para representar los tipos de pisos '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Materiales de Pisos"

class TipoBanio(models.Model):
    ''' Modelo para representar los tipos de baños '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Baño"

class TipoInodoro(models.Model):
    ''' Modelo para representar los tipos de inodoros '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Tipos de Inodoros"

class UsoVivienda(models.Model):
    ''' Modelo para representar los usos de la vivienda '''
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Usos de la Vivienda"

class Encuesta(models.Model):
    ''' Modelo para representar las encuestas '''
    fecha = models.DateField(default=datetime.now)
    encuestadore = models.ForeignKey(User, models.CASCADE, blank=True, null=True, verbose_name='Cargado por')
    direccion = models.CharField(max_length=100)
    manzanaRENABAP = models.CharField(max_length=10, blank=True, null=True)
    loteRENABAP = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.direccion}"

    class Meta:
        verbose_name_plural = "1-Encuestas"

class Familia(models.Model):
    ''' Modelo para representar las personas de la familias encuestadas '''
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    parentezco = models.ForeignKey(Parentezco, models.CASCADE)
    edad = models.IntegerField()
    genero = models.ForeignKey(Genero, models.CASCADE, blank=True, null=True)
    nacionalidad = models.ForeignKey(Nacionalidad, models.CASCADE)
    dniArgentino = models.BooleanField()
    concurreEscuela = models.BooleanField()
    establecimientoEducativo = models.ForeignKey(Institucion, models.CASCADE, related_name="famEstEduc", blank=True, null=True)
    centroFormacion = models.ForeignKey(Institucion, models.CASCADE, related_name="famEstForm", blank=True, null=True)
    establecimientoCuidados = models.ForeignKey(Institucion, models.CASCADE, related_name="famEstCuida", blank=True, null=True)
    tieneDiscapacidad = models.BooleanField()
    tieneCertificadoDiscapacidad = models.BooleanField()
    leeEscribe = models.BooleanField()

    def __str__(self):
        return f"{self.parentezco} - {self.edad}"

    class Meta:
        verbose_name_plural = "2-Familiares"

class Trabajo(models.Model):
    ''' Modelo para representar la situación laboral de las personas de la familias encuestadas '''
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    familia = models.ForeignKey(Familia, models.CASCADE)
    tieneTrabajo = models.BooleanField()
    aportaJubilación = models.BooleanField()
    tipoTrabajo = models.ForeignKey(TipoTrabajo, models.CASCADE, related_name="traTipo", blank=True, null=True)
    jubiladxPensionadx = models.BooleanField()
    percibeAsignaciones = models.BooleanField()

    def __str__(self):
        return f"Situación laboral {self.encuesta} - {self.familia}"

    class Meta:
        verbose_name_plural = "3-Situación laboral"

class Vivienda(models.Model):
    ''' Modelo para representar la situación de vivienda de la familias encuestadas '''
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    tipoVivienda = models.ForeignKey(TipoVivienda, models.CASCADE, related_name="vivTipo", blank=True, null=True)
    materialesPiso= models.ForeignKey(MaterialesPiso, models.CASCADE, related_name="vivTipoPiso", blank=True, null=True)
    materialesPared = models.ForeignKey(MaterialesPared, models.CASCADE, related_name="vivTipoPared", blank=True, null=True)
    materialesTecho = models.ForeignKey(MaterialesTecho, models.CASCADE, related_name="vivTipoTecho", blank=True, null=True)
    tipoBanio = models.ForeignKey(TipoBanio, models.CASCADE, related_name="vivTipoBa", blank=True, null=True)
    tipoInodoro = models.ForeignKey(TipoInodoro, models.CASCADE, related_name="vivTipoIn", blank=True, null=True, verbose_name="Tipo de Baño")
    cantidadHabitantes = models.IntegerField()
    habitacionesPernocte = models.IntegerField()
    usoVivienda = models.ForeignKey(UsoVivienda, models.CASCADE, related_name="vivUso", blank=True, null=True)
    tiempoHabita = models.IntegerField()
    tieneCertificado = models.BooleanField()

    def __str__(self):
        return f"Tipo de vivienda {self.encuesta} - {self.tipoVivienda}"

    class Meta:
        verbose_name_plural = "4-Situación vivienda"

class Servicios(models.Model):
    ''' Modelo para representar la situación de servicios públicos de la vivienda '''
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    luz = models.ForeignKey(OpcionesLuz, models.CASCADE, related_name="vivTipo", blank=True, null=True)
    agua= models.ForeignKey(OpcionesAgua, models.CASCADE, related_name="vivTipoPiso", blank=True, null=True)
    gas = models.ForeignKey(OpcionesGas, models.CASCADE, related_name="vivTipoPared", blank=True, null=True)
    cloacas = models.ForeignKey(OpcionesCloacas, models.CASCADE, related_name="vivTipoTecho", blank=True, null=True)
    cortesFataPago = models.BooleanField()
    tarifaSocial = models.BooleanField()
    recoleccionResiduos = models.ForeignKey(OpcionesResiduos, models.CASCADE, related_name="vivResid", blank=True, null=True)

    def __str__(self):
        return f"Servicios Públicos {self.encuesta}"

    class Meta:
        verbose_name_plural = "5-Servicios Públicos"

class InfraSocial(models.Model):
    ''' Modelo para representar la situación de infraestructura social de soporte '''
    frecuencia = (
        ('1S', '1 vez a la semana'),
        ('2S', '2 veces a la semana'),
        ('+2S', 'Más de 2 veces a la semana'),
        ('1M', '1 vez al mes'),
        ('1A', '1 vez al año'),
        ('CM', 'Circunstancialmente'),
    )
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    espaciosPoderosa = models.ManyToManyField(EspaciosPoderosa, related_name="infraEspacios", verbose_name="A que espacios de LP asiste")
    centrosSalud = models.BooleanField()
    atencionPostaSalud = models.BooleanField()
    turnosPostaSalud = models.BooleanField()
    frecuenciaAtencionSalud = models.CharField(max_length=3, choices=frecuencia, blank=True, null=True, default='1', verbose_name='Frecuencia de asistencia a Centros de Salud')
    experienciaAtencion = models.TextField(blank=True, null=True)
    problemasCronicosFamiliares = models.BooleanField()
    lugaresAtencion = models.TextField(blank=True, null=True)
    ambulanciaIngresa = models.BooleanField()
    
    def __str__(self):
        return f"Infraestructura Social {self.encuesta}"

    class Meta:
        verbose_name_plural = "6-Infraestructura Social"