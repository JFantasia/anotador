from datetime import datetime

from django.db import models

# Create your models here.
from persona.models import Persona
from parametros.models import Etiqueta, Genero, Localidad, TipoIntervecion, Institucion
from parametros_salud.models import Cobertura, Enfermedad, Dificultad, Especialidad, PresionArterial, Medicamento
from parametros_salud.models import VeNumerosLetras, IdentificaColores, TestVistaLejos, TestVistaCerca, Autopercepcion, EnfermedadCronica
from parametros_salud.models import SituacionVivienda, MaterialVivienda, ServicioVivienda



class Profesional(models.Model):
    ''' Modelo para representar les profesionales de la salud '''
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    documento = models.CharField(max_length=8, unique=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    piso_dpto = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=20, blank=True, null=True)
    localidad = models.ForeignKey(Localidad, models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    especialidad = models.ManyToManyField(Especialidad, related_name="esmed")

    def __str__(self):
        return f"{self.documento} - {self.apellido}, {self.nombre}"

    class Meta:
        verbose_name_plural = "Profesionales"

class Ficha(models.Model):
    ''' Modelo para representar las fichas de salud de las personas en la plataforma '''
    persona = models.ForeignKey(Persona, models.CASCADE, related_name= "sfp")
    genero = models.ForeignKey(Genero, models.CASCADE, related_name= "sfg")
    cobertura = models.ForeignKey(Cobertura, models.CASCADE, null=True, blank=True)
    nro_afiliade = models.CharField(max_length=50, null=True, blank=True)
    medicos = models.ManyToManyField(Profesional, related_name="medcab", blank=True)
    enfermedades_cronicas = models.ManyToManyField(EnfermedadCronica, related_name="enf_cronicas", blank=True)
    dificultades = models.ManyToManyField(Dificultad, related_name="dif", blank=True)
    situacion_vivienda = models.ManyToManyField(SituacionVivienda, blank=True)
    materiales_vivienda = models.ManyToManyField(MaterialVivienda, blank=True)
    servicios_vivienda = models.ManyToManyField(ServicioVivienda, blank=True)
    ambientes_vivienda = models.IntegerField(null=True, blank=True)
    hijes = models.IntegerField(null=True, blank=True)
    convivientes_vivienda = models.IntegerField(null=True, blank=True)

    ingreso = models.DateField()

    def __str__(self):
        return f"{self.persona}"

    class Meta:
        verbose_name_plural = "Fichas"

class Atencion(models.Model):
    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE)
    persona = models.ForeignKey(Ficha, models.CASCADE)
    detalle = models.TextField()
    presion = models.ForeignKey(PresionArterial, models.CASCADE, null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    identifica_letras = models.ForeignKey(VeNumerosLetras, models.CASCADE, null=True, blank=True)
    identifica_colores = models.ForeignKey(IdentificaColores, models.CASCADE, null=True, blank=True)
    test_cerca = models.ForeignKey(TestVistaCerca, models.CASCADE, null=True, blank=True)
    test_lejos = models.ForeignKey(TestVistaLejos, models.CASCADE, null=True, blank=True)
    autopercepcion = models.ForeignKey(Autopercepcion, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Atenciones"

class Intervencion(models.Model):
    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE, related_name="sti", limit_choices_to={'app__nombre': 'Salud'})
    institucion = models.ForeignKey(Institucion, models.CASCADE, related_name="stin")
    persona = models.ForeignKey(Ficha, models.CASCADE)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.persona}"

    class Meta:
        verbose_name_plural = "Intervenciones"

class Lista_Medicamentos(models.Model):

    ''' Modelo para representar las Intervenciones de salud de las personas en la plataforma '''
    atencion = models.ForeignKey(Atencion, models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, models.CASCADE)
    entregado = models.BooleanField()
    detalle = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.atencion} - {self.medicamento}"

    class Meta:
        verbose_name_plural = "Medicamentos Entregados/Recetados"

estados = [
    ('P','Pendiente'),
    ('F','Finalizada'),
    ('C','Cancelada'),
]
class AgendaTurnos(models.Model):
    ''' Modelo para representar las agendas de turnos por tipo y fecha '''
    fecha = models.DateField()
    hora_desde= models.TimeField(default=datetime.time(datetime.now()))
    hora_hasta = models.TimeField(default=datetime.time(datetime.now()))
    tipo = models.ForeignKey(TipoIntervecion, models.CASCADE, related_name="atti")
    profesional = models.ForeignKey(Profesional, models.CASCADE, related_name="atpe")
    detalle = models.TextField(null=True, blank=True)
    estado = models.CharField('Estado', max_length=1, choices=estados, default='P')

    # def save(self, *args, **kwargs):
    #     if self.hora_desde < self.hora_hasta:
    #         super().save(*args, **kwargs)
    #     else:
    #         print("Rango horario erroneo")
    #         raise ValidationError('Rango horario erroneo')

    def __str__(self):
        return f"{self.fecha} - {self.tipo}, {self.profesional}"

    class Meta:
        verbose_name_plural = "Agenda de turnos"

class Turno(models.Model):
    ''' Modelo para representar los turnos de una agenda '''
    agenda = models.ForeignKey(AgendaTurnos, models.CASCADE)
    ficha = models.ForeignKey(Ficha, models.CASCADE, related_name="atfi")
    hora = models.TimeField()
    sobreturno = models.BooleanField(null=True, blank=True)
    asistio = models.BooleanField(null=True, blank=True)
    atencion = models.ForeignKey(Atencion, models.CASCADE, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.agenda} - {self.ficha}, {self.hora}"

    class Meta:
        verbose_name_plural = "Turnos"

class Nota(models.Model):
    ''' Modelo para representar las notas de salud '''
    fecha = models.DateField()
    etiqueta = models.ForeignKey(Etiqueta, models.CASCADE, related_name= "nes", null=True, blank=True)
    resumen = models.CharField(max_length=50)
    detalle = models.TextField()


    def __str__(self):
        return f"{self.fecha} - {self.resumen}"

    class Meta:
        verbose_name_plural = "Notas"

class Turno_Externos(models.Model):
    ''' Modelo para representar los turnos en consultorios / centros de salud externos '''
    ficha = models.ForeignKey(Ficha, models.CASCADE, related_name="fiturex")
    fecha = models.DateField()
    hora = models.TimeField()
    centro_salud = models.ForeignKey(Institucion, models.CASCADE, null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, models.CASCADE, null=True, blank=True)
    profesional = models.ForeignKey(Profesional, models.CASCADE, null=True, blank=True)
    asistio = models.BooleanField(null=True, blank=True)
    demanda_insatisfecha = models.BooleanField(null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.ficha} - {self.fecha}, {self.profesional}"

    class Meta:
        verbose_name_plural = "Turnos Externos"