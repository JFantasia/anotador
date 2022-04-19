from django.contrib import admin

# Register your models here.
from salud.models import Ficha, Intervencion

admin.site.register(Ficha)

class IntervencionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'tipo', 'persona']
    list_filter = ['fecha', 'tipo', 'persona__persona__documento']

admin.site.register(Intervencion, IntervencionAdmin)
