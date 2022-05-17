from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Ficha, Lista_Espera, Intervencion

# Register your models here.
class FichaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['persona', 'programa', 'unidad_productiva']
    list_filter = ['unidad_productiva', 'programa', 'estado_programa', 'estado_persona']

admin.site.register(Ficha, FichaAdmin)

admin.site.register(Lista_Espera)
admin.site.register(Intervencion)