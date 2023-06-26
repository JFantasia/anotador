from django import forms

from .models import Familia, Trabajo


class TrabajoForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (TrabajoForm,self ).__init__(*args,**kwargs) # populates the post
        print(list(self.fields['encuesta']._get_choices()))
        self.fields['familia'].queryset = Familia.objects.filter(encuesta=self.fields['encuesta'])

    class Meta:
        model = Trabajo
        fields = "__all__"