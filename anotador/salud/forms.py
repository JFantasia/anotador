from datetime import datetime

from django import forms

from .models import AgendaTurnos, Turno


class AgendaTurnosForm(forms.ModelForm):
    class Meta:
        model = AgendaTurnos
        fields = '__all__'

    # Validación de horario desde / hasta.

    def clean(self):
        if self.cleaned_data.get('hora_desde') >= self.cleaned_data.get('hora_hasta'):
            raise forms.ValidationError('Rango horario erroneo para desde / hasta')


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

    # Validación de horario desde / hasta.

    def clean(self):
        print(self.cleaned_data.get('hora'))
        print(self.cleaned_data.get('agenda').hora_desde)

        if self.cleaned_data.get('hora') > self.cleaned_data.get('agenda').hora_hasta or self.cleaned_data.get('hora') < self.cleaned_data.get('agenda').hora_desde :
            raise forms.ValidationError('Horario del turno fuera de rango de la agenda: ' + str(self.cleaned_data.get('agenda').hora_desde) + " - " + str(self.cleaned_data.get('agenda').hora_hasta))