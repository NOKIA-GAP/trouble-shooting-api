from django import forms
from django.forms import ModelForm
from .models import (
Alerta
)
from . import choices

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

class AlertaForm(ModelForm):
    estado_oferta = forms.ChoiceField(choices=choices.ESTADO_ALERTA_CHOICES, required=True)

    class Meta:
        model = Alerta
        fields = ('estado_alerta',)

    def clean(self):
        cleaned_data = super(AlertaForm, self).clean()
        alerta = self.instance

        if estado_oferta == CERRADO:
            alerta.delete()

        return cleaned_data
