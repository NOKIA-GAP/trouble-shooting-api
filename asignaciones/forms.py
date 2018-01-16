# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from .models import (
AsignacionNpo,
AsignacionNi,
)
from users.models import Perfil
from . import choices
from troubleshooting import settings
from notificaciones.models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
)

ASIGNADA = 'Asignada'
EN_MONITOREO = 'En monitoreo'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
REQUIERE_VISITA = 'Requiere visita'
NO_EXITOSA = 'No exitosa'
ESCALADO_A_CLARO = 'Escalado a claro'

INSTALACION = 'Instalacion'
INTEGRACION = 'Integracion'

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
    asignar_par = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input','style':'margin-left: 100px'}), required=False)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.ni_asignador = kwargs.pop('ni_asignador', None)
        super(AsignacionNiForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNi
        fields = ('ni_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion', 'asignar_par')

    def clean(self):
        cleaned_data = super(AsignacionNiForm, self).clean()
        ni_ingeniero = cleaned_data.get('ni_ingeniero')
        asignar_par = cleaned_data.get('asignar_par')
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
        if asignar_par:
            try:
                asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
                actividad=actividad,
                estado_asignacion=ASIGNADA,
                )
                raise forms.ValidationError('la Actividad ya fue asignada a par NPO')
            except AsignacionNpo.DoesNotExist:
                pass
            try:
                asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
                actividad=actividad,
                estado_asignacion=EN_MONITOREO,
                )
                raise forms.ValidationError('la Actividad ya fue asignada a par NPO y se encuentra en monitoreo')
            except AsignacionNpo.DoesNotExist:
                pass
        return cleaned_data

class AsignacionNiAsignadorForm(ModelForm):
    ni_ingeniero = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='NI Ingeniero'), required=True)
    fm_supervisor = forms.ModelChoiceField(queryset=Perfil.objects.filter(perfil_usuario='FM Supervisor'), required=False)
    tipo_intervencion = forms.ChoiceField(choices=choices.TIPO_INTERVENCION_CHOICES, required=True)
    # fecha_asignacion = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    asignar_par = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input','style':'margin-left: 100px'}), required=False)

    def __init__(self, *args, **kwargs):
        self.actividad = kwargs.pop('actividad', None)
        self.ni_asignador = kwargs.pop('ni_asignador', None)
        super(AsignacionNiAsignadorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AsignacionNi
        fields = ('ni_ingeniero', 'fm_supervisor', 'tipo_intervencion', 'fecha_asignacion', 'asignar_par')
        widgets = {
            'fecha_asignacion': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date', 'required':'true'}),
        }

    def clean(self):
        cleaned_data = super(AsignacionNiAsignadorForm, self).clean()
        ni_ingeniero = cleaned_data.get('ni_ingeniero')
        asignar_par = cleaned_data.get('asignar_par')
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
        if asignar_par:
            try:
                asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
                actividad=actividad,
                estado_asignacion=ASIGNADA,
                )
                raise forms.ValidationError('la Actividad ya fue asignada a par NPO')
            except AsignacionNpo.DoesNotExist:
                pass
            try:
                asignacion_npo_asignanada_actividad = AsignacionNpo.objects.get(
                actividad=actividad,
                estado_asignacion=EN_MONITOREO,
                )
                raise forms.ValidationError('la Actividad ya fue asignada a par NPO y se encuentra en monitoreo')
            except AsignacionNpo.DoesNotExist:
                pass
        return cleaned_data

class AsignacionNiIngenieroForm(ModelForm):
    estado_asignacion = forms.ChoiceField(choices=choices.ESTADO_ASIGNACION_CHOICES, required=True)
    origen_falla = forms.ChoiceField(choices=choices.ORIGEN_FALLA_CHOICES, required=False)
    # origen_falla = forms.ChoiceField(widget=forms.HiddenInput(), choices=choices.ORIGEN_FALLA_CHOICES, required=False)
    solver = forms.ChoiceField(choices=choices.SOLVER_CHOICES, required=False)

    class Meta:
        model = AsignacionNi
        fields = ('estado_asignacion',
                  'origen_falla',
                  'detalle_falla_instalacion',
                  'detalle_solicitud_visita',
                  'solver')

    def clean(self):
        cleaned_data = super(AsignacionNiIngenieroForm, self).clean()
        conceptos = self.instance.conceptos_ni.all()
        estado_asignacion = cleaned_data.get('estado_asignacion')
        origen_falla = cleaned_data.get('origen_falla')
        detalle_falla_instalacion = cleaned_data.get('detalle_falla_instalacion')
        detalle_solicitud_visita = cleaned_data.get('detalle_solicitud_visita')
        solver = cleaned_data.get('solver')
        estacion = self.instance.estacion
        actividad = self.instance.actividad
        service_supplier = self.instance.actividad.service_supplier
        ni_ingeniero = self.instance.ni_ingeniero

        if not conceptos:
            raise forms.ValidationError('La asignacion no tiene un Concepto.')

        if estado_asignacion == REQUIERE_VISITA:

            send_mail(
                'Requiere Visita' +' '+
                estacion.nombre +' '+
                actividad.banda +' '+
                actividad.proyecto +' '+
                actividad.escenario,

                'Buen día Señores '+ service_supplier +'\n'+'\n'+
                'Se informa que el equipo Nokia realizará visita correctiva atendiendo es escalamiento del NOC producto de la actividad mencionada en el asunto. \
                De encontrarse falla de instalación se realizará el reporte para proceder con el conducto regular para este tipo de casos.' +'\n'+'\n'+

                'Detalle Solicitud Visita:' +'\n'+'\n'+

                detalle_solicitud_visita +'\n'+'\n'+

                'Ingeniero Nokia: '+ ni_ingeniero.nombre_completo.title() +'\n'+'\n'+

                'Cordial Saludo,' +'\n'+'\n'+

                'OnAir Team' +'\n'+'\n'+

                'NOTA: Este es un mensaje de prueba para el estado de asignacion Requiere visita. \
                Y esta es una lista provisional será oficial en W4.',

                'notification_onair.noreply@nokia.com',

                ['jbri.gap@nokia.com',
                'juan.andrade@nokia.com',
                'jorge.baracaldo@nokia.com',
                'ivan.jimenez_robayo@nokia.com',
                'dtor.onair_claro@nokia.com',
                'jsan.onair_claro@nokia.com'],
                fail_silently=False,
            )
            NotificacionRequiereVisita.objects.create(
                asignacion_ni=self.instance,
                actividad=actividad,
                wp=actividad.wp,
                service_supplier=actividad.service_supplier,
                estacion=estacion,
                banda=actividad.banda,
                proyecto=actividad.proyecto,
                escenario=actividad.escenario,
                ni_ingeniero=ni_ingeniero,
                detalle_solicitud_visita=detalle_solicitud_visita,
            )

        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == INSTALACION:

            send_mail(
                'Falla Instalacion' +' '+
                estacion.nombre +' '+
                actividad.banda +' '+
                actividad.proyecto +' '+
                actividad.escenario,

                'Buen día Señores '+ service_supplier +'\n'+'\n'+

                detalle_falla_instalacion +'\n'+'\n'+

                'Ingeniero Nokia: '+ ni_ingeniero.nombre_completo.title() +'\n'+'\n'+

                'Solver: '+ solver +'\n'+'\n'+

                'Cordial Saludo,' +'\n'+'\n'+

                'OnAir Team' +'\n'+'\n'+

                'NOTA: Este es un mensaje de prueba para origen falla Instalacion. \
                Y esta es una lista provisional será oficial en W4.',

                'notification_onair.noreply@nokia.com',

                ['jbri.gap@nokia.com',
                'juan.andrade@nokia.com',
                'jorge.baracaldo@nokia.com',
                'ivan.jimenez_robayo@nokia.com',
                'dtor.onair_claro@nokia.com',
                'jsan.onair_claro@nokia.com'],
                fail_silently=False,
            )
            NotificacionFallaInstalacion.objects.create(
                asignacion_ni=self.instance,
                actividad=actividad,
                wp=actividad.wp,
                service_supplier=actividad.service_supplier,
                estacion=estacion,
                banda=actividad.banda,
                proyecto=actividad.proyecto,
                escenario=actividad.escenario,
                ni_ingeniero=ni_ingeniero,
                detalle_falla_instalacion=detalle_falla_instalacion,
                solver=solver,
            )

        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == INTEGRACION:

            send_mail(
                'Falla Integracion' +' '+
                estacion.nombre +' '+
                actividad.banda +' '+
                actividad.proyecto +' '+
                actividad.escenario,

                'Buen día Ivan Jimenez' +'\n'+'\n'+
                
                conceptos.last().contenido +'\n'+'\n'+

                'Ingeniero Nokia: '+ ni_ingeniero.nombre_completo.title() +'\n'+'\n'+

                'Service Supplier: '+ service_supplier +'\n'+'\n'+

                'Cordial Saludo,' +'\n'+'\n'+

                'OnAir Team' +'\n'+'\n'+

                'NOTA: Este es un mensaje de prueba para origen falla Integracion. \
                Y esta es una lista provisional será oficial en W4.',

                'notification_onair.noreply@nokia.com',

                ['jbri.gap@nokia.com',
                'juan.andrade@nokia.com',
                'jorge.baracaldo@nokia.com',
                'ivan.jimenez_robayo@nokia.com',
                'dtor.onair_claro@nokia.com',
                'jsan.onair_claro@nokia.com'],
                fail_silently=False,
            )
            NotificacionFallaIntegracion.objects.create(
                asignacion_ni=self.instance,
                actividad=actividad,
                wp=actividad.wp,
                service_supplier=actividad.service_supplier,
                estacion=estacion,
                banda=actividad.banda,
                proyecto=actividad.proyecto,
                escenario=actividad.escenario,
                ni_ingeniero=ni_ingeniero,
                concepto=conceptos.last().contenido,
            )

        return cleaned_data
