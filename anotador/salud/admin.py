from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin

from .forms import AgendaTurnosForm, TurnoForm
from .models import Ficha, Intervencion, Atencion, Lista_Medicamentos, AgendaTurnos, Nota, Turno




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


class AtencionesTabularInline(admin.TabularInline):
    model = Atencion
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
    list_filter = ['genero', 'cobertura', 'ingreso']
    inlines = [IntervencionesTabularInline, AtencionesTabularInline]

admin.site.register(Ficha, FichaAdmin)
admin.site.register(Lista_Medicamentos)

class IntervencionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'persona']
    list_filter = ['fecha', 'tipo', 'persona__persona__documento']

admin.site.register(Intervencion, IntervencionAdmin)

class MedicamentosTabularInline(admin.TabularInline):
    model = Lista_Medicamentos
    can_delete = True

class AtencionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'persona']
    list_filter = ['fecha', 'tipo', 'persona__persona__documento']
    inlines = [MedicamentosTabularInline]

admin.site.register(Atencion, AtencionAdmin)

class TurnoAdmin(ExportActionMixin, admin.ModelAdmin):
    form = TurnoForm
    list_display = ['agenda', 'hora', 'ficha']
    list_filter = ['hora']

admin.site.register(Turno, TurnoAdmin)

class TurnosTabularInline(admin.TabularInline):
    model = Turno
    fields = ('ficha', 'hora')
    can_delete = True

class AgendaTurnosAdmin(admin.ModelAdmin):
    form = AgendaTurnosForm
    model = AgendaTurnos
    list_display = ['fecha', 'tipo', 'estado']
    list_filter = ['fecha', 'tipo', 'estado']
    inlines = [TurnosTabularInline]

    # def has_add_permission(self, request):
    #     print(request)
    #
    # def has_change_permission(self, request, obj=None):
    #     if self.model.get('estado') == "F":
    #         return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     if self.model.get('estado') == "F":
    #         return False

admin.site.register(AgendaTurnos, AgendaTurnosAdmin)

class NotaAdmin(ExportActionMixin, admin.ModelAdmin):
    # list_display = ['persona', 'tipo', 'persona']
    list_filter = ['etiqueta']

admin.site.register(Nota, NotaAdmin)