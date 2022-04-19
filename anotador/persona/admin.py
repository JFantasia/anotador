from django.contrib import admin

# Register your models here.
from persona.models import Grupo, Persona

admin.site.register(Grupo)
admin.site.register(Persona)