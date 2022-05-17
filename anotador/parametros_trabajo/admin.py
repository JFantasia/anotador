from django.contrib import admin
from .models import UnidadProductiva, Dependencia, Programa, Trabajo, Rama, Actividad
# Register your models here.

admin.site.register(UnidadProductiva)
admin.site.register(Dependencia)
admin.site.register(Programa)
admin.site.register(Trabajo)
admin.site.register(Actividad)
class ActividadTabularInline(admin.TabularInline):
    model = Actividad
    can_delete = True

class RamaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ('nombre',)
    inlines = [ActividadTabularInline]

admin.site.register(Rama, RamaAdmin)

