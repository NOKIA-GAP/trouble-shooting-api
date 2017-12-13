# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import SolicitudHW, Solicitud
from . import choices
from django.forms.models import inlineformset_factory

REQUIEREHW = 'Requiere HW'
HWSOLICITADO = 'HW solicitado'

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
        solicitudes = asignacion_ni.solicitudeshw.all()

        # if solicitudes:
        #     for solicitud in solicitudes:
        #         print solicitud.estado_solicitud
        #         if solicitud.estado_solicitud == REQUIEREHW or solicitud.estado_solicitud == HWSOLICITADO:
        #             raise forms.ValidationError('Para esta asignacion ya existe una Solicitud.')
        if solicitudes:
            for solicitud in solicitudes:
                if (solicitud.estado_solicitud == 'HW recibido'):
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
