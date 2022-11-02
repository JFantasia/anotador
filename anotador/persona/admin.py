import json
# from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin
from persona.models import Grupo, Persona
# from django.core import serializers


admin.site.register(Grupo)

class PersonaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['documento', 'nombre', 'apellido', 'telefono']
    list_filter = ['calle', 'grupo']
    '''
    Código para prueba de gráficos
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Persona.objects.all()
        )
        chart_data_all = Persona.objects.all()
        
        # Serialize and attach the chart data to the template context
        # as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        as_json = serializers.serialize("json",chart_data_all)
        print(as_json)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
    '''

admin.site.register(Persona, PersonaAdmin)