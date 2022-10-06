from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin

from .models import Ficha, Intervencion, Nota

class IntervencionesTabularInline(admin.TabularInline):
    model = Intervencion
    fields = ('fecha', 'tipo', 'detalle')
    can_delete = False
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FichaAdmin(ExportActionMixin, admin.ModelAdmin):
    # list_display = ['persona', 'tipo', 'persona']
    list_filter = ['situacion_violencia', 'situacion_habitacional', 'situacion_familiar',
    'situacion_justicia', 'situacion_salud', 'situacion_consumo']
    inlines = [IntervencionesTabularInline]

admin.site.register(Ficha, FichaAdmin)

class IntervencionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'persona']
    list_filter = ['fecha', 'tipo', 'persona__persona__documento']

admin.site.register(Intervencion, IntervencionAdmin)

class NotaAdmin(ExportActionMixin, admin.ModelAdmin):
    # list_display = ['persona', 'tipo', 'persona']
    list_filter = ['etiqueta']

admin.site.register(Nota, NotaAdmin)
