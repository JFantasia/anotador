from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin
from persona.models import Grupo, Persona

admin.site.register(Grupo)

class PersonaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['documento', 'nombre', 'apellido', 'telefono']
    list_filter = ['calle', 'grupo']

admin.site.register(Persona, PersonaAdmin)