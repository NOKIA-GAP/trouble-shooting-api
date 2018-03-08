from django import forms
from django.forms import ModelForm
from .models import (
Alerta
)
from . import choices

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

class AlertaForm(ModelForm):
    estado_alerta = forms.ChoiceField(choices=choices.ESTADO_ALERTA_CHOICES, required=True)

    class Meta:
        model = Alerta
        fields = ('estado_alerta',)

    # def clean(self):
    #     cleaned_data = super(AlertaForm, self).clean()
    #     estado_alerta = cleaned_data.get('estado_alerta')
    #     alerta = self.instance
    #
    #     if estado_alerta == CERRADO:
    #         alerta.delete()
    #
    #     return cleaned_data
