from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin

from .models import Organizacion, Reserva, Tarea, TipoEspacio, Espacio, Recurso, TipoTarea

class EspacioTabularInline(admin.TabularInline):
    model = Espacio
    fields = ('nombre', 'tipo', 'ciudad')
    can_delete = False
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrganizacionAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [EspacioTabularInline]

admin.site.register(Organizacion, OrganizacionAdmin)

class RecursosTabularInline(admin.TabularInline):
    model = Recurso
    fields = ('identificacion', 'etiqueta', 'espacio')
    can_delete = False
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class EspacioAdmin(ExportActionMixin, admin.ModelAdmin):
    inlines = [RecursosTabularInline]

admin.site.register(Espacio, EspacioAdmin)

class RecursoAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['identificacion', 'etiqueta', 'espacio']
    list_filter = ['etiqueta', 'espacio']

admin.site.register(Recurso, RecursoAdmin)

admin.site.register(TipoEspacio)
admin.site.register(TipoTarea)

class ReservaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'solicitantes', 'detalle']
    list_filter = ['solicitantes', 'fecha']

admin.site.register(Reserva, ReservaAdmin)

class TareaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['tipo', 'nombre', 'estado', 'limite']
    list_filter = ['estado', 'limite']

admin.site.register(Tarea, TareaAdmin)