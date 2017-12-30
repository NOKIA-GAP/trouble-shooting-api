# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import (
AsignacionNpo,
AsignacionNi,
)
from users.models import Perfil
from . import choices
from troubleshooting import settings

ASIGNADA = 'Asignada'
EN_MONITOREO = 'En monitoreo'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
REQUIERE_VISITA = 'Requiere visita'
NO_EXITOSA = 'No exitosa'
ESCALADO_A_CLARO = 'Escalado a claro'

NI_ASIGNADOR = 'NI Asignador'
NPO_ASIGNADOR = 'NPO Asignador'
FM_LIDER = 'FM Lider'
GAP_ADMINISTRADOR = 'GAP Administrador'

class AsignacionNpoForm(ModelForm):
    npo_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NPO Ingeniero'), required=True)
    fm_supervisor = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='FM Supervisor'), required=False)
    tipo_intervencion = forms.ChoiceField(choices=choices.TIPO_INTERVENCION_CHOICES, required=True)
    fecha_asignacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=True)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.npo_asignador = kwargs.pop('npo_asignador', None)
        super(AsignacionNpoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNpo
        fields = ('npo_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion')

    def clean(self):
        cleaned_data = super(AsignacionNpoForm, self).clean()
        npo_ingeniero = cleaned_data.get('npo_ingeniero')
        actividad = self.actividad
        npo_asignador = self.npo_asignador

        if (npo_asignador.perfil_usuario == NPO_ASIGNADOR
            or npo_asignador.perfil_usuario == FM_LIDER
            or npo_asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            actividad=actividad,
            estado_asignacion=ASIGNADA,
            )
            raise forms.ValidationError('la Actividad ya fue asignada.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            actividad=actividad,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('la Actividad se encuentra en monitoreo.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignada = AsignacionNpo.objects.get(
            actividad=actividad,
            npo_ingeniero=npo_ingeniero,
            estado_asignacion=ASIGNADA,
            )
            raise forms.ValidationError('para este NPO ingeniero la Actividad ya fue asignada.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_en_monitoreo = AsignacionNpo.objects.get(
            actividad=actividad,
            npo_ingeniero=npo_ingeniero,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('para este NPO ingeniero la Actividad se encuentra en monitoreo.')
        except AsignacionNpo.DoesNotExist:
            pass
        return cleaned_data

class AsignacionNpoAsiganadorForm(ModelForm):
    npo_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NPO Ingeniero'), required=True)
    fm_supervisor = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='FM Supervisor'), required=False)
    tipo_intervencion = forms.ChoiceField(choices=choices.TIPO_INTERVENCION_CHOICES, required=True)
    fecha_asignacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=True)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.npo_asignador = kwargs.pop('npo_asignador', None)
        super(AsignacionNpoAsiganadorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNpo
        fields = ('npo_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion')

    def clean(self):
        cleaned_data = super(AsignacionNpoAsiganadorForm, self).clean()
        npo_ingeniero = cleaned_data.get('npo_ingeniero')
        actividad = self.actividad
        npo_asignador = self.npo_asignador
        pk = self.instance.pk

        if (npo_asignador.perfil_usuario == NPO_ASIGNADOR
            or npo_asignador.perfil_usuario == FM_LIDER
            or npo_asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('la Actividad se encuentra En monitoreo.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=ENVIADO_A_SEGUIMIENTO,
            )
            raise forms.ValidationError('la Actividad se encuentra Enviado a seguimiento.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=REQUIERE_VISITA,
            )
            raise forms.ValidationError('la Actividad se encuentra Requiere visita.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=NO_EXITOSA,
            )
            raise forms.ValidationError('la Actividad se encuentra No exitosa.')
        except AsignacionNpo.DoesNotExist:
            pass
        try:
            asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=ESCALADO_A_CLARO,
            )
            raise forms.ValidationError('la Actividad se encuentra Escalado a claro.')
        except AsignacionNpo.DoesNotExist:
            pass
        return cleaned_data


class AsignacionNpoIngenieroForm(ModelForm):
    estado_asignacion = forms.ChoiceField(choices=choices.ESTADO_ASIGNACION_CHOICES, required=True)

    class Meta:
        model = AsignacionNpo
        fields = ('estado_asignacion',)

    def clean(self):
        cleaned_data = super(AsignacionNpoIngenieroForm, self).clean()
        conceptos = self.instance.conceptos_npo.all()

        if not conceptos:
            raise forms.ValidationError('La asignacion no tiene un Concepto.')

        return cleaned_data

class AsignacionNiForm(ModelForm):
    ni_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NI Ingeniero'), required=True)
    fm_supervisor = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='FM Supervisor'), required=False)
    tipo_intervencion = forms.ChoiceField(choices=choices.TIPO_INTERVENCION_CHOICES, required=True)
    fecha_asignacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=True)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.ni_asignador = kwargs.pop('ni_asignador', None)
        super(AsignacionNiForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNi
        fields = ('ni_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion')

    def clean(self):
        cleaned_data = super(AsignacionNiForm, self).clean()
        ni_ingeniero = cleaned_data.get('ni_ingeniero')
        actividad = self.actividad
        ni_asignador = self.ni_asignador

        if (ni_asignador.perfil_usuario == NI_ASIGNADOR
            or ni_asignador.perfil_usuario == FM_LIDER
            or ni_asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')

        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            actividad=actividad,
            estado_asignacion=ASIGNADA,
            )
            raise forms.ValidationError('la Actividad ya fue asignada')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            actividad=actividad,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('la Actividad se encuentra en monitoreo')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignada = AsignacionNi.objects.get(
            actividad=actividad,
            ni_ingeniero=ni_ingeniero,
            estado_asignacion=ASIGNADA,
            )
            raise forms.ValidationError('para este NI ingeniero la Actividad ya fue asignada')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_en_monitoreo = AsignacionNi.objects.get(
            actividad=actividad,
            ni_ingeniero=ni_ingeniero,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('para este NI ingeniero la Actividad se encuentra en monitoreo')
        except AsignacionNi.DoesNotExist:
            pass
        return cleaned_data

class AsignacionNiAsignadorForm(ModelForm):
    ni_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NI Ingeniero'), required=True)
    fm_supervisor = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='FM Supervisor'), required=False)
    tipo_intervencion = forms.ChoiceField(choices=choices.TIPO_INTERVENCION_CHOICES, required=True)
    fecha_asignacion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=True)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.ni_asignador = kwargs.pop('ni_asignador', None)
        super(AsignacionNiAsignadorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNi
        fields = ('ni_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion')

    def clean(self):
        cleaned_data = super(AsignacionNiAsignadorForm, self).clean()
        ni_ingeniero = cleaned_data.get('ni_ingeniero')
        actividad = self.actividad
        ni_asignador = self.ni_asignador
        pk = self.instance.pk

        if (ni_asignador.perfil_usuario == NI_ASIGNADOR
            or ni_asignador.perfil_usuario == FM_LIDER
            or ni_asignador.perfil_usuario == GAP_ADMINISTRADOR):
            pass
        else:
            raise forms.ValidationError('Su perfil no esta habilitado para asignar.')
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=EN_MONITOREO,
            )
            raise forms.ValidationError('la Actividad se encuentra En monitoreo.')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=ENVIADO_A_SEGUIMIENTO,
            )
            raise forms.ValidationError('la Actividad se encuentra Enviado a seguimiento.')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=REQUIERE_VISITA,
            )
            raise forms.ValidationError('la Actividad se encuentra Requiere visita.')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=NO_EXITOSA,
            )
            raise forms.ValidationError('la Actividad se encuentra No exitosa.')
        except AsignacionNi.DoesNotExist:
            pass
        try:
            asignacion_ni_asignanada_actividad = AsignacionNi.objects.get(
            id=pk,
            actividad=actividad,
            estado_asignacion=ESCALADO_A_CLARO,
            )
            raise forms.ValidationError('la Actividad se encuentra Escalado a claro.')
        except AsignacionNi.DoesNotExist:
            pass
        return cleaned_data

class AsignacionNiIngenieroForm(ModelForm):
    estado_asignacion = forms.ChoiceField(choices=choices.ESTADO_ASIGNACION_CHOICES, required=True)
    origen_falla = forms.ChoiceField(choices=choices.ORIGEN_FALLA_CHOICES, required=True)
    # origen_falla = forms.ChoiceField(widget=forms.HiddenInput(), choices=choices.ORIGEN_FALLA_CHOICES, required=False)

    class Meta:
        model = AsignacionNi
        fields = ('estado_asignacion', 'origen_falla')

    def clean(self):
        cleaned_data = super(AsignacionNiIngenieroForm, self).clean()
        conceptos = self.instance.conceptos_ni.all()

        if not conceptos:
            raise forms.ValidationError('La asignacion no tiene un Concepto.')

        return cleaned_data

# <div class="form-group">
# {{ form|crispy }}
# {% for visible_field in form.visible_fields %}
# {{ visible_field }}
# {% if visible_field.value == "Asignada" %}
# <h1>{{ visible_field.value }}</h1>
# {% endif %}
# {% endfor %}
# {% for hidden_field in form.hidden_fields %}
# {{ hidden_field }}
# {% endfor %}
# </div>
