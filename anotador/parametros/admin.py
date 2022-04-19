from django.contrib import admin

# Register your models here.
from parametros.models import Pais, Provincia, Ciudad, Aplicacion, Sexo, Genero, TipoIntervecion

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Aplicacion)
admin.site.register(Sexo)
admin.site.register(Genero)
admin.site.register(TipoIntervecion)
