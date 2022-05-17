from django.contrib import admin

# Register your models here.
from .models import Pais, Provincia, Ciudad, Aplicacion, Genero, TipoIntervecion, Localidad, Nacionalidad

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Localidad)
admin.site.register(Nacionalidad)
admin.site.register(Aplicacion)
admin.site.register(Genero)
admin.site.register(TipoIntervecion)
