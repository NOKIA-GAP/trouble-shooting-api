# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import (
Actividad,
Degradacion,
)
from troubleshooting import settings
from django.contrib.auth.models import Permission
from . import choices


class ActividadForm(ModelForm):
    # fecha_ingreso_onair = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)
    # realtifinish = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)
    # fecha_integracion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)
    # po_solicitud = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)
    # fecha_estado_noc = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)
    # fecha_fc_visita = forms.DateField(widget=forms.DateInput(attrs={'class':'form-inline','type':'date'}), input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ActividadForm, self).__init__(*args, **kwargs)

        all_perm = Permission.objects.all()

        # Default
        if not user.is_superuser and not user.has_perm(all_perm):
            if user.perfil.perfil_usuario == None:
                # self.fields.pop('wp')
                self.fields.pop('id_notificacion_noc')
                # self.fields.pop('agrupador')
                # self.fields.pop('service_supplier')
                # self.fields.pop('estacion')
                # self.fields.pop('banda')
                # self.fields.pop('valor_wp_eur')
                # self.fields.pop('proyecto')
                # self.fields.pop('escenario')
                self.fields.pop('tipo_trabajo')
                self.fields.pop('fecha_ingreso_onair')
                self.fields.pop('realtifinish')
                self.fields.pop('fecha_integracion')
                self.fields.pop('grupo_gap')
                self.fields.pop('ss_tbs')
                self.fields.pop('po_solicitud')
                self.fields.pop('fecha_estado_noc')
                self.fields.pop('estado_noc')
                self.fields.pop('subestado_noc')
                self.fields.pop('impacto_degradacion')
                self.fields.pop('fecha_fc_visita')
                self.fields.pop('tipo_intervencion')
                self.fields.pop('requiere_hw')
                self.fields.pop('cantidad_hw')
                # self.fields.pop('estado')
                # self.fields.pop('subestado')

        #Administrador
        if user.is_superuser and user.has_perm(all_perm):
            self.fields

        # GAP Administrador
        if not user.is_superuser and user.has_perm("users.perm_gap_administrador"):
            self.fields

        # NI Ingeniero
        if not user.is_superuser and user.has_perm("users.perm_ni_ingeniero"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('ss_tbs')
            self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')
            # self.fields.pop('requiere_hw')
            # self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')

        # NI Asignador
        if not user.is_superuser and user.has_perm("users.perm_ni_asignador"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('ss_tbs')
            self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            # self.fields.pop('estado_noc')
            # self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')
            self.fields.pop('requiere_hw')
            self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')

        # NPO Ingeniero
        if not user.is_superuser and user.has_perm("users.perm_npo_ingeniero"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('ss_tbs')
            self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            # self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')
            # self.fields.pop('requiere_hw')
            self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')

        # NPO Asignador
        if not user.is_superuser and user.has_perm("users.perm_npo_asignador"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('ss_tbs')
            self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            # self.fields.pop('impacto_degradacion')
            # self.fields.pop('fecha_fc_visita')
            # self.fields.pop('requiere_hw')
            self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')

        # FM Lider
        if not user.is_superuser and user.has_perm("users.perm_fm_lider"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            # self.fields.pop('ss_tbs')
            # self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            # self.fields.pop('fecha_fc_visita')
            # self.fields.pop('tipo_intervencion')
            # self.fields.pop('requiere_hw')
            # self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')

        # FM Permisos
        if not user.is_superuser and user.has_perm("users.perm_fm_permisos"):
            # self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            # self.fields.pop('agrupador')
            # self.fields.pop('service_supplier')
            # self.fields.pop('estacion')
            # self.fields.pop('banda')
            # self.fields.pop('valor_wp_eur')
            # self.fields.pop('proyecto')
            # self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('ss_tbs')
            self.fields.pop('po_solicitud')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')
            self.fields.pop('requiere_hw')
            self.fields.pop('cantidad_hw')
            # self.fields.pop('estado')
            # self.fields.pop('subestado')



    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'fecha_ingreso_onair': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'realtifinish': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'fecha_integracion': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'po_solicitud': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'fecha_estado_noc': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
            'fecha_fc_visita': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
        }

    # def clean(self):
    #
    #     goa = 'GAP On Air'
    #     gi = 'GAP Integracion'
    #     p = 'Produccion'
    #     date = timezone.now()
    #     tipo_gap = self.cleaned_data.get('tipo_gap')
    #     fecha_integracion = self.cleaned_data.get('fecha_integracion')
    #     estado_noc = self.cleaned_data.get('estado_noc')
    #     fecha_primera_respuesta_npo = self.cleaned_data.get('fecha_primera_respuesta_npo')
    #     _concepto_ni = self.instance.concepto_ni
    #     concepto_ni = self.cleaned_data.get('concepto_ni')
    #     fecha_concepto_ni = self.cleaned_data.get('fecha_concepto_ni')
    #
    #     if not fecha_concepto_ni and concepto_ni: # si es actualizado primera vez
    #         self.cleaned_data['fecha_concepto_ni'] = date #fecha actual
    #
    #     if fecha_concepto_ni and concepto_ni != _concepto_ni: # si es actualizada
    #         self.cleaned_data['fecha_concepto_ni'] = date #fecha actual
    #
    #     if not fecha_primera_respuesta_npo: #si no esta
    #         self.cleaned_data['fecha_primera_respuesta_npo'] = date #fecha actual
    #
    #     if fecha_integracion and estado_noc == 'Produccion':
    #         self.cleaned_data['tipo_gap'] = p
    #
    #     if fecha_integracion and estado_noc != 'Produccion':
    #         self.cleaned_data['tipo_gap'] = goa
    #
    #     else:
    #         self.cleaned_data['tipo_gap'] = gi
    #
    #         return self.cleaned_data


class DegradacionForm(ModelForm):

    class Meta:
        model = Degradacion
        fields = ('contenido',)
