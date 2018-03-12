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
                self.fields.pop('wp')
                self.fields.pop('id_notificacion_noc')
                self.fields.pop('agrupador')
                self.fields.pop('service_supplier')
                self.fields.pop('field_manager')
                self.fields.pop('valor_wp_eur')
                self.fields.pop('estacion')
                self.fields.pop('banda')
                self.fields.pop('proyecto')
                self.fields.pop('escenario')
                self.fields.pop('tipo_trabajo')
                self.fields.pop('fecha_ingreso_onair')
                self.fields.pop('realtifinish')
                self.fields.pop('fecha_integracion')
                self.fields.pop('grupo_gap')
                self.fields.pop('fecha_estado_noc')
                self.fields.pop('estado_noc')
                self.fields.pop('subestado_noc')
                self.fields.pop('impacto_degradacion')
                self.fields.pop('fecha_fc_visita')

        #Administrador
        if user.is_superuser and user.has_perm(all_perm):
            self.fields

        # GAP Administrador
        if not user.is_superuser and user.has_perm("users.perm_gap_administrador"):
            self.fields

        # NI Ingeniero
        if not user.is_superuser and user.has_perm("users.perm_ni_ingeniero"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')

        # NI Asignador
        if not user.is_superuser and user.has_perm("users.perm_ni_asignador"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            # self.fields.pop('estado_noc')
            # self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')

        # NPO Ingeniero
        if not user.is_superuser and user.has_perm("users.perm_npo_ingeniero"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            # self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')

        # NPO Asignador
        if not user.is_superuser and user.has_perm("users.perm_npo_asignador"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            # self.fields.pop('impacto_degradacion')
            # self.fields.pop('fecha_fc_visita')

        # FM Lider
        if not user.is_superuser and user.has_perm("users.perm_fm_lider"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            # self.fields.pop('fecha_fc_visita')

        # FM Permisos
        if not user.is_superuser and user.has_perm("users.perm_fm_permisos"):
            self.fields.pop('wp')
            self.fields.pop('id_notificacion_noc')
            self.fields.pop('agrupador')
            self.fields.pop('service_supplier')
            self.fields.pop('field_manager')
            self.fields.pop('valor_wp_eur')
            self.fields.pop('estacion')
            self.fields.pop('banda')
            self.fields.pop('proyecto')
            self.fields.pop('escenario')
            self.fields.pop('tipo_trabajo')
            self.fields.pop('fecha_ingreso_onair')
            self.fields.pop('realtifinish')
            self.fields.pop('fecha_integracion')
            self.fields.pop('grupo_gap')
            self.fields.pop('fecha_estado_noc')
            self.fields.pop('estado_noc')
            self.fields.pop('subestado_noc')
            self.fields.pop('impacto_degradacion')
            self.fields.pop('fecha_fc_visita')

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

class DegradacionForm(ModelForm):

    class Meta:
        model = Degradacion
        fields = ('contenido',)
