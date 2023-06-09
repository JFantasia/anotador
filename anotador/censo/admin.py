from django.contrib import admin

from censo.models import EspaciosPoderosa, InfraSocial, MaterialesPared, MaterialesPiso, MaterialesTecho, OpcionesAgua, OpcionesCloacas, OpcionesGas, OpcionesLuz, Parentezco, Encuesta, Familia, TipoBanio, TipoInodoro, TipoTrabajo, TipoVivienda, Trabajo, UsoVivienda, Vivienda, Servicios

admin.site.register(Parentezco)
admin.site.register(Familia)
admin.site.register(Trabajo)
admin.site.register(Vivienda)
admin.site.register(Servicios)
admin.site.register(InfraSocial)
admin.site.register(EspaciosPoderosa)
admin.site.register(TipoTrabajo)
admin.site.register(OpcionesLuz)
admin.site.register(OpcionesAgua)
admin.site.register(OpcionesGas)
admin.site.register(OpcionesCloacas)
admin.site.register(TipoVivienda)
admin.site.register(MaterialesTecho)
admin.site.register(MaterialesPared)
admin.site.register(MaterialesPiso)
admin.site.register(TipoBanio)
admin.site.register(TipoInodoro)
admin.site.register(UsoVivienda)


class FamiliaInline(admin.TabularInline):
    model = Familia
    fields = ('parentezco', 'edad')

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class TrabajoInline(admin.TabularInline):
    model = Trabajo
    fields = ('familia', 'tieneTrabajo', 'tipoTrabajo')

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ViviendaInline(admin.TabularInline):
    model = Vivienda
    fields = ('tipoVivienda', 'cantidadHabitantes', 'usoVivienda')

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ServiciosInline(admin.TabularInline):
    model = Servicios
    fields = ('luz', 'agua', 'gas', 'cloacas')

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class InfraSocialInline(admin.TabularInline):
    model = InfraSocial
    fields = ('espaciosPoderosa', 'centrosSalud', 'atencionPostaSalud')

    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'direccion', 'encuestadore']
    list_filter = ['encuestadore', 'fecha']
    inlines = [FamiliaInline, TrabajoInline, ViviendaInline, ServiciosInline, InfraSocialInline]


admin.site.register(Encuesta, EncuestaAdmin)