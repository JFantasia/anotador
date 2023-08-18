from django.contrib import admin

from import_export.admin import ExportActionMixin

from .models import Articulo, DetalleEntrega, DetalleRecepcion, Entrega, Recepcion, TipoArticulo


# Register your models here.

admin.site.register(TipoArticulo)

class ArticuloAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['nombre', 'tipoArticulo', 'stock']
    list_filter = ['esAlimento', 'esRopa', 'esMaterial']
    readonly_fields = ['stock']

admin.site.register(Articulo, ArticuloAdmin)


@admin.action(description="Completar Recepción de Artículos")
def completar_recepcion(modeladmin, request, queryset):
    queryset.update(estado="C")
    for obj in queryset:
        prods = DetalleRecepcion.objects.filter(recepcion=obj)
        for prod in prods:
            prod.articulo.stock += prod.cantidad
            prod.articulo.save()

@admin.action(description="Completar Entrega de Artículos")
def completar_entrega(modeladmin, request, queryset):
    queryset.update(estado="C")
    for obj in queryset:
        prods = DetalleEntrega.objects.filter(entrega=obj)
        for prod in prods:
            prod.articulo.stock -= prod.cantidad
            prod.articulo.save()


class DetalleEntregaInline(admin.TabularInline):
    model = DetalleEntrega
    fields = ('articulo', 'cantidad')

class EntregaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'estado', 'referencia']
    list_filter = ['estado', 'grupo']
    actions = [completar_entrega]
    inlines = [DetalleEntregaInline]
    readonly_fields = ['estado']

admin.site.register(Entrega, EntregaAdmin)



class DetalleRecepcionInline(admin.TabularInline):
    model = DetalleRecepcion
    fields = ('articulo', 'cantidad')



class RecepcionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['fecha', 'estado', 'referencia']
    list_filter = ['estado', 'grupo']
    actions = [completar_recepcion]
    inlines = [DetalleRecepcionInline]
    readonly_fields = ['estado']

admin.site.register(Recepcion, RecepcionAdmin)