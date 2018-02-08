# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import SolicitudHW, Solicitud
from . import choices
from django.forms.models import inlineformset_factory

REQUIEREHW = 'Requiere HW'
HWSOLICITADO = 'HW solicitado'
HWRECIBIDO = 'HW recibido'

class SolicitudHWUpdateForm(ModelForm):
    estado_solicitud = forms.ChoiceField(choices=choices.ESTADO_SOLICITUD_CHOICES)

    class Meta:
        model = SolicitudHW
        fields = ('estado_solicitud',)

class SolicitudHWForm(ModelForm):
    estado_solicitud = forms.ChoiceField(choices=choices.ESTADO_SOLICITUD_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        self.asignacion_ni = kwargs.pop('asignacion_ni', None)
        super(SolicitudHWForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SolicitudHW
        fields = ('estado_solicitud',)

    def clean(self):
        cleaned_data = super(SolicitudHWForm, self).clean()
        asignacion_ni = self.asignacion_ni
        actividad = asignacion_ni.actividad
        solicitudes_asignacion = asignacion_ni.solicitudeshw.all()
        solicitudes_actividad = actividad.solicitudeshw.all()

        if solicitudes_actividad:
            for solicitud in solicitudes_actividad:
                if solicitud.actividad == actividad and solicitud.estado_solicitud != HWRECIBIDO:
                    raise forms.ValidationError('Para esta actividad ya existe una Solicitud.')

        if solicitudes_asignacion:
            for solicitud in solicitudes_asignacion:
                if solicitud.estado_solicitud == HWRECIBIDO:
                    pass
                else:
                    raise forms.ValidationError('Para esta asignacion ya existe una Solicitud.')

        return cleaned_data

class SolicitudForm(ModelForm):
    hardware = forms.ChoiceField(choices=choices.HARDWARE_CHOICES, required=True)

    class Meta:
        model = Solicitud
        fields = ('hardware', 'cantidad', 'descripcion',)

SolicitudFormSet = inlineformset_factory(SolicitudHW, Solicitud,
                                         form=SolicitudForm, extra=1)
