from django import forms
from django.forms import ModelForm
from .models import (
IncidenteNpo,
IncidenteNi,
)
from users.models import Perfil
from . import choices

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'
FM_LIDER = 'FM Lider'
GAP_ADMINISTRADOR = 'GAP Administrador'

class IncidenteNpoForm(ModelForm):
    npo_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NPO Ingeniero'), required=True)

    def __init__(self, *args, **kwargs):
        self.asignador = kwargs.pop('asignador', None)
        self.actividad = kwargs.pop('actividad', None)
        super(IncidenteNpoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = IncidenteNpo
        fields = ('npo_ingeniero',)

    def clean(self):
        cleaned_data = super(IncidenteNpoForm, self).clean()
        asignador = self.asignador
        actividad = self.actividad
        if (asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')
        try:
            incidente_npo_asignanada_actividad = IncidenteNpo.objects.get(
            actividad=actividad,
            estado_incidente=ABIERTO,
            )
            raise forms.ValidationError('la Actividad tiene un incidente NPO Abierto.')
        except IncidenteNpo.DoesNotExist:
            pass
        return cleaned_data


class IncidenteIngenieroNpoForm(ModelForm):
    estado_incidente = forms.ChoiceField(choices=choices.ESTADO_INCIDENTE_CHOICES, required=True)
    # comentario = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = IncidenteNpo
        fields = ('estado_incidente',)

    def clean(self):
        cleaned_data = super(IncidenteIngenieroNpoForm, self).clean()
        comentarios = self.instance.comentarios_npo.all()

        if not comentarios:
            raise forms.ValidationError('El incidente no tiene un Comentario.')

        return cleaned_data

class IncidenteNiForm(ModelForm):
    ni_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NI Ingeniero'), required=True)
    asignar_par = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    # asignar_par = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input','style':'margin-left: 100px'}), required=False)

    def __init__(self, *args, **kwargs):
        self.asignador = kwargs.pop('asignador', None)
        self.actividad = kwargs.pop('actividad', None)
        super(IncidenteNiForm, self).__init__(*args, **kwargs)

    class Meta:
        model = IncidenteNi
        fields = ('ni_ingeniero', 'asignar_par')

    def clean(self):
        cleaned_data = super(IncidenteNiForm, self).clean()
        asignador = self.asignador
        actividad = self.actividad
        asignar_par = cleaned_data.get('asignar_par')
        if (asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')
        try:
            incidente_ni_asignanada_actividad = IncidenteNi.objects.get(
            actividad=actividad,
            estado_incidente=ABIERTO,
            )
            raise forms.ValidationError('la Actividad tiene un incidente NI Abierto.')
        except IncidenteNi.DoesNotExist:
            pass
        if asignar_par:
            try:
                incidente_ni_asignanada_actividad = IncidenteNpo.objects.get(
                actividad=actividad,
                estado_incidente=ABIERTO,
                )
                raise forms.ValidationError('el par tiene un incidente NPO Abierto para esta actividad.')
            except IncidenteNpo.DoesNotExist:
                pass
        return cleaned_data

class IncidenteIngenieroNiForm(ModelForm):
    estado_incidente = forms.ChoiceField(choices=choices.ESTADO_INCIDENTE_CHOICES, required=True)
    # comentario = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = IncidenteNi
        fields = ('estado_incidente',)

    def clean(self):
        cleaned_data = super(IncidenteIngenieroNiForm, self).clean()
        comentarios = self.instance.comentarios_ni.all()

        if not comentarios:
            raise forms.ValidationError('El incidente no tiene un Comentario.')

        return cleaned_data
