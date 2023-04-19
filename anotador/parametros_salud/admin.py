from django.contrib import admin

from .models import Cobertura, Enfermedad, Dificultad, ElementoCuidado, Especialidad, ProblematicaBarrio, Medicamento
from .models import SituacionVivienda, MaterialVivienda, ServicioVivienda
from .models import EnfermedadCronica
from .models import PresionArterial, IdentificaColores, VeNumerosLetras, TestVistaCerca, TestVistaLejos, Autopercepcion

# Register your models here.

admin.site.register(Cobertura)
admin.site.register(Enfermedad)
admin.site.register(EnfermedadCronica)
admin.site.register(Dificultad)
admin.site.register(ElementoCuidado)
admin.site.register(ProblematicaBarrio)
admin.site.register(PresionArterial)

admin.site.register(IdentificaColores)
admin.site.register(VeNumerosLetras)
admin.site.register(TestVistaCerca)
admin.site.register(TestVistaLejos)
admin.site.register(Autopercepcion)
admin.site.register(Medicamento)

admin.site.register(SituacionVivienda)
admin.site.register(MaterialVivienda)
admin.site.register(ServicioVivienda)
admin.site.register(Especialidad)
