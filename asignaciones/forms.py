# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail, EmailMessage
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
NotificacionFallaMalRechazo,
)
from fallas.models import (
Falla
)

ASIGNADA = 'Asignada'
EN_MONITOREO = 'En monitoreo'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
REQUIERE_VISITA = 'Requiere visita'
NO_EXITOSA = 'No exitosa'
ESCALADO_A_CLARO = 'Escalado a claro'

INSTALACION = 'Instalacion'
SOFTWARE = 'Software'
HARDWARE = 'Hardware'
DATAFILL = 'Datafill'
AJUSTEPOTENCIA = 'Ajuste Potencia'
INTEGRACION = 'Integracion'
INTERFERENCIAEXTREMA = 'Interferencia externa'
CAMBIODISENO = 'Cambio diseno'
MALRECHAZO = 'Mal rechazo'
TX = 'TX'
COMPORTAMIENTOESPERADO = 'Comportamiento esperado'
COMPORTAMIENTOPREVIO = 'Comportamiento previo'
AJUSTEADYACENCIAS = 'Ajuste Adyacencias'

NI_ASIGNADOR = 'NI Asignador'
NPO_ASIGNADOR = 'NPO Asignador'
FM_LIDER = 'FM Lider'
GAP_ADMINISTRADOR = 'GAP Administrador'

CENTRO = 'Centro'
ORIENTE = 'Oriente'
SUROCCIDENTE = 'Sur Occidente'
NOROCCIDENTE = 'Nor Occidente'
COSTA = 'Costa'
NORORIENTE = 'Nor Oriente'

ADSM = 'ADSM'
DECOM = 'DECOM'
DELTEC = 'DELTEC'
EZENTIS = 'EZENTIS'
FIBRATERRA = 'FIBRATERRA'
GAMMA = 'GAMMA'
INGETEL = 'INGETEL'
INGYTELCOM = 'INGYTELCOM'
JANACOR = 'JANACOR'
MSI = 'MSI'
OSC = 'OSC'
REDESYSERVICIOS = 'REDES Y SERVICIOS'
RSE = 'RSE'
SAI = 'SAI'
SERVINTELCO = 'SERVINTELCO'
SITCOM = 'SITCOM'
YINDA = 'YINDA'
ZOOM = 'ZOOM'
INMEL = 'INMEL'

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
    # asignar_par = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input','style':'margin-left: 100px'}), required=False)
    asignar_par = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

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
    # asignar_par = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input','style':'margin-left: 100px'}), required=False)
    asignar_par = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

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
        regional = estacion.regional
        ni_ingeniero = self.instance.ni_ingeniero

        if not conceptos:
            raise forms.ValidationError('La asignacion no tiene un Concepto.')

        if estado_asignacion == REQUIERE_VISITA:

            asunto = 'Notificación Escalamiento NOC' +' '+ \
            estacion.nombre +' '+ \
            actividad.banda +' '+ \
            actividad.proyecto +' '+ \
            actividad.escenario +' '+ \
            'WP:' +' '+ \
            str(actividad.wp)

            contenido = 'Buen día Señores '+ service_supplier +'\n'+'\n'+ 'Se informa \
            que el equipo Nokia realizará visita correctiva atendiendo escalamiento del \
            NOC producto de la actividad mencionada en el asunto. \
            De encontrarse falla de instalación se realizará el reporte para proceder \
            con el conducto regular para este tipo de casos.' +'\n'+'\n'+ \
            'Detalle Solicitud Visita:' +'\n'+'\n'+ detalle_solicitud_visita +'\n'+'\n'+ \
            'Ingeniero Nokia: ' + ni_ingeniero.nombre_completo.title() +'\n'+'\n'+ \
            'Cordial Saludo,' +'\n'+'\n'+ 'OnAir Team'

            de = 'notification_onair.noreply@gaponair.com'

            para_regional = []

            if regional == CENTRO or regional == ORIENTE:
                para_regional = ['andres.montano@nokia.com', 'mng1.claro@nokia.com']
            if regional == COSTA or regional == NORORIENTE:
                para_regional = ['hubert.tafurt_hidalgo@nokia.com', 'rom1.claro@nokia.com']
            if regional == SUROCCIDENTE or regional == NOROCCIDENTE:
                para_regional = ['rafael.garcia@nokia.com', 'fernando.franco_soto@nokia.com']

            para_ss = []

            if service_supplier == ADSM:
                para_ss = [
                          'davidsaavedra@adsm.com.co',
                          'magdaburbano@adsm.com.co',
                          'williamgrillo@adsm.com.co',
                          'heillerjimenez@adsm.com.co',
                          'gustavo@adsm.com.co',
                          ]
            if service_supplier == DECOM:
                para_ss = [
                          'edwin.castrillon@decom.com.co',
                          'miguel.lopez@decom.com.co',
                          ]
            if service_supplier == DELTEC:
                para_ss = [
                          'gbonilla@deltec.com.co',
                          'salvarado@deltec.com.co',
                          'jquintana@deltec.com.co',
                          'aescobar@deltec.com.co',
                          'aarana@deltec.com.co',
                          ]
            if service_supplier == EZENTIS:
                para_ss = [
                          'edison.santos@ezentis.com.co',
                          'fabio.cardenasr@ezentis.com.co',
                          'javier.amorocho@ezentis.com.co',
                          ]
            if service_supplier == FIBRATERRA:
                para_ss = [
                          'coordinador1@fibraterra.com',
                          'fernando.ramirez@fibraterra.com',
                          'msarmiento@fibraterra.com',
                          'lyda.ramirez@fibraterra.com',
                          ]
            if service_supplier == GAMMA:
                para_ss = [
                          'diego.vargas@gammasg.com',
                          'andres.bonilla@gammasg.com',
                          'paola.garzon@gammasg.com',
                          'josedomingo.gomez@gammasg.com',
                          ]
            if service_supplier == INGETEL:
                para_ss = [
                          'supervision_cali@ingetelsas.com.co',
                          'supervision@ingetelsas.com.co',
                          'auditor@ingetelsas.com.co',
                          'gerencia@ingetelsas.com.co',
                          'administrativo@ingetelsas.com.co',
                          ]
            if service_supplier == INGYTELCOM:
                para_ss = [
                          'diana.pineda@ingytelcom.com',
                          'robinson.lopez@ingytelcom.com',
                          'cindy.lopez@ingytelcom.com.co',
                          'cristian.organista@ingytelcom.com',
                          'javier.orjuela@ingytelcom.com',
                          'cbardet@ingytelcom.com',
                          ]
            if service_supplier == JANACOR:
                para_ss = [
                          'ingeniero@janacor.co',
                          'liliana.cristancho@janacor.co',
                          ]
            if service_supplier == MSI:
                para_ss = [
                          'david.Osorio@msiamericas.com',
                          'elizabeth.baron@msiamericas.com',
                          'rafael.riano@msiamericas.com',
                          ]
            if service_supplier == OSC:
                para_ss = [
                          'Jose.fuquene@osctelecoms.com',
                          'marcela.rodriguez@osctelecoms.com',
                          'angelica.dharo@osctelecoms.com',
                          'andres.pacheco@osctelecoms.com',
                          'julieth.caceres@osctelecoms.com',
                          'esther.villegas@osctelecoms.com',
                          ]
            if service_supplier == REDESYSERVICIOS:
                para_ss = [
                          'jheisson.alvarez@rseltda.com',
                          'rene.sanchez@rseltda.com',
                          'jonnathan.cubillos@rseltda.com',
                          'ibeth.quijano@rseltda.com',
                          ]
            if service_supplier == RSE:
                para_ss = [
                          'jheisson.alvarez@rseltda.com',
                          'rene.sanchez@rseltda.com',
                          'jonnathan.cubillos@rseltda.com',
                          'ibeth.quijano@rseltda.com',
                          ]
            if service_supplier == SAI:
                para_ss = [
                          'operaciones@saisas.com.co',
                          'proyectos@saisas.com.co',
                          'gerencia@saisas.com.co',
                          'gerente.administracion@saisas.com.co',
                          ]
            if service_supplier == SERVINTELCO:
                para_ss = [
                          'erick.amaya@servintelco.com',
                          'carlos.bateman@servintelco.com',
                          ]
            if service_supplier == SITCOM:
                para_ss = [
                          'maricela.rodriguez@sitcom.co',
                          'alejandro.pinzon@sitcom.co',
                          'daniel.valderrama@sitcom.co',
                          'ivan.diaz@sitcom.co',
                          ]
            if service_supplier == YINDA:
                para_ss = [
                          'john.maldonado@yinda.com.co',
                          'oscar.acosta@yinda.com.co',
                          'torsten.kroeger@yindacorp.com',
                          'kari.nikkinen@yinda.com.co',
                          'leonardo.alarcon@yinda.com.co',
                          ]
            if service_supplier == ZOOM:
                para_ss = [
                          'coord.proy.nk@zoom-cgr.com',
                          'vladimiryanes@zoom-cgr.com',
                          'hrestrepo@zoom-cgr.com',
                          'waltermolina@zoom-cgr.com',
                          ]
            if service_supplier == INMEL:
                para_ss = [
                          'miguel.lopez@inmel.com.co'
                          ]

            para = para_regional + para_ss

            copia = ['jbri.gap@nokia.com',
                    'I_EXT_GAP_CLARO_COL@nokia.com',
                    'I_EXT_FIELD_MANAGEMENT_CLARO_COL@nokia.com',
                    'jorge.baracaldo@nokia.com',
                    'leopoldo.morales_cabrales@nokia.com',
                    'fred.rodriguez@nokia.com',
                    'omar.gugliesi@nokia.com']

            email = EmailMessage(asunto, contenido, de, para, cc=copia)
            email.send(fail_silently=False)

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

            asunto = 'Falla Instalacion' +' '+ \
            estacion.nombre +' '+ \
            actividad.banda +' '+ \
            actividad.proyecto +' '+ \
            actividad.escenario +' '+ \
            'WP:' +' '+ \
            str(actividad.wp)

            contenido = 'Buen día Señores '+ service_supplier +'\n'+'\n'+ \
            detalle_falla_instalacion +'\n'+'\n'+ \
            'Ingeniero Nokia: ' + ni_ingeniero.nombre_completo.title() +'\n'+'\n'+ \
            'Solver: '+ solver +'\n'+'\n'+ \
            'Cordial Saludo,' +'\n'+'\n'+ 'OnAir Team'

            de = 'notification_onair.noreply@gaponair.com'

            para_regional = []

            if regional == CENTRO or regional == ORIENTE:
                para_regional = ['andres.montano@nokia.com', 'mng1.claro@nokia.com']
            if regional == COSTA or regional == NORORIENTE:
                para_regional = ['hubert.tafurt_hidalgo@nokia.com', 'rom1.claro@nokia.com']
            if regional == SUROCCIDENTE or regional == NOROCCIDENTE:
                para_regional = ['rafael.garcia@nokia.com', 'fernando.franco_soto@nokia.com']

            para_ss = []

            if service_supplier == ADSM:
                para_ss = [
                          'davidsaavedra@adsm.com.co',
                          'magdaburbano@adsm.com.co',
                          'williamgrillo@adsm.com.co',
                          'heillerjimenez@adsm.com.co',
                          'gustavo@adsm.com.co',
                          ]
            if service_supplier == DECOM:
                para_ss = [
                          'edwin.castrillon@decom.com.co',
                          'miguel.lopez@decom.com.co',
                          ]
            if service_supplier == DELTEC:
                para_ss = [
                          'gbonilla@deltec.com.co',
                          'salvarado@deltec.com.co',
                          'jquintana@deltec.com.co',
                          'aescobar@deltec.com.co',
                          'aarana@deltec.com.co',
                          ]
            if service_supplier == EZENTIS:
                para_ss = [
                          'edison.santos@ezentis.com.co',
                          'fabio.cardenasr@ezentis.com.co',
                          'javier.amorocho@ezentis.com.co',
                          ]
            if service_supplier == FIBRATERRA:
                para_ss = [
                          'coordinador1@fibraterra.com',
                          'fernando.ramirez@fibraterra.com',
                          'msarmiento@fibraterra.com',
                          'lyda.ramirez@fibraterra.com',
                          ]
            if service_supplier == GAMMA:
                para_ss = [
                          'diego.vargas@gammasg.com',
                          'andres.bonilla@gammasg.com',
                          'paola.garzon@gammasg.com',
                          'josedomingo.gomez@gammasg.com',
                          ]
            if service_supplier == INGETEL:
                para_ss = [
                          'supervision_cali@ingetelsas.com.co',
                          'supervision@ingetelsas.com.co',
                          'auditor@ingetelsas.com.co',
                          'gerencia@ingetelsas.com.co',
                          'administrativo@ingetelsas.com.co',
                          ]
            if service_supplier == INGYTELCOM:
                para_ss = [
                          'diana.pineda@ingytelcom.com',
                          'robinson.lopez@ingytelcom.com',
                          'cindy.lopez@ingytelcom.com.co',
                          'cristian.organista@ingytelcom.com',
                          'javier.orjuela@ingytelcom.com',
                          'cbardet@ingytelcom.com',
                          ]
            if service_supplier == JANACOR:
                para_ss = [
                          'ingeniero@janacor.co',
                          'liliana.cristancho@janacor.co',
                          ]
            if service_supplier == MSI:
                para_ss = [
                          'david.Osorio@msiamericas.com',
                          'elizabeth.baron@msiamericas.com',
                          'rafael.riano@msiamericas.com',
                          ]
            if service_supplier == OSC:
                para_ss = [
                          'Jose.fuquene@osctelecoms.com',
                          'marcela.rodriguez@osctelecoms.com',
                          'angelica.dharo@osctelecoms.com',
                          'andres.pacheco@osctelecoms.com',
                          'julieth.caceres@osctelecoms.com',
                          'esther.villegas@osctelecoms.com',
                          ]
            if service_supplier == REDESYSERVICIOS:
                para_ss = [
                          'jheisson.alvarez@rseltda.com',
                          'rene.sanchez@rseltda.com',
                          'jonnathan.cubillos@rseltda.com',
                          'ibeth.quijano@rseltda.com',
                          ]
            if service_supplier == RSE:
                para_ss = [
                          'jheisson.alvarez@rseltda.com',
                          'rene.sanchez@rseltda.com',
                          'jonnathan.cubillos@rseltda.com',
                          'ibeth.quijano@rseltda.com',
                          ]
            if service_supplier == SAI:
                para_ss = [
                          'operaciones@saisas.com.co',
                          'proyectos@saisas.com.co',
                          'gerencia@saisas.com.co',
                          'gerente.administracion@saisas.com.co',
                          ]
            if service_supplier == SERVINTELCO:
                para_ss = [
                          'erick.amaya@servintelco.com',
                          'carlos.bateman@servintelco.com',
                          ]
            if service_supplier == SITCOM:
                para_ss = [
                          'maricela.rodriguez@sitcom.co',
                          'alejandro.pinzon@sitcom.co',
                          'daniel.valderrama@sitcom.co',
                          'ivan.diaz@sitcom.co',
                          ]
            if service_supplier == YINDA:
                para_ss = [
                          'john.maldonado@yinda.com.co',
                          'oscar.acosta@yinda.com.co',
                          'torsten.kroeger@yindacorp.com',
                          'kari.nikkinen@yinda.com.co',
                          'leonardo.alarcon@yinda.com.co',
                          ]
            if service_supplier == ZOOM:
                para_ss = [
                          'coord.proy.nk@zoom-cgr.com',
                          'vladimiryanes@zoom-cgr.com',
                          'hrestrepo@zoom-cgr.com',
                          'waltermolina@zoom-cgr.com',
                          ]
            if service_supplier == INMEL:
                para_ss = [
                          'miguel.lopez@inmel.com.co'
                          ]

            para = para_regional + para_ss

            copia = ['jbri.gap@nokia.com',
                    'I_EXT_GAP_CLARO_COL@nokia.com',
                    'I_EXT_FIELD_MANAGEMENT_CLARO_COL@nokia.com',
                    'jorge.baracaldo@nokia.com',
                    'leopoldo.morales_cabrales@nokia.com',
                    'fred.rodriguez@nokia.com',
                    'omar.gugliesi@nokia.com',
                    'john.guerrero_rivera@nokia.com',
                    'jose.herrera_gomez@nokia.com',
                    'maria_fernanda.pacheco@nokia.com']

            email = EmailMessage(asunto, contenido, de, para, cc=copia)
            email.send(fail_silently=False)

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
            Falla.objects.create(
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
                tipo_falla=INSTALACION,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == INTEGRACION:

            asunto = 'Falla Integracion' +' '+ \
            estacion.nombre +' '+ \
            actividad.banda +' '+ \
            actividad.proyecto +' '+ \
            actividad.escenario +' '+ \
            'WP:' +' '+ \
            str(actividad.wp)

            contenido = 'Buen día Ivan Jimenez' +'\n'+'\n'+ \
            conceptos.last().contenido +'\n'+'\n'+ \
            'Ingeniero Nokia: ' + ni_ingeniero.nombre_completo.title() +'\n'+'\n'+ \
            'Service Supplier: '+ service_supplier +'\n'+'\n'+ \
            'Cordial Saludo,' +'\n'+'\n'+ 'OnAir Team'

            de = 'notification_onair.noreply@gaponair.com'

            para = ['ivan.jimenez_robayo@nokia.com']

            copia = ['jbri.gap@nokia.com',
                    'I_EXT_GAP_CLARO_COL@nokia.com',
                    'jorge.baracaldo@nokia.com',
                    'dtor.onair_claro@nokia.com',
                    'jsan.onair_claro@nokia.com']

            email = EmailMessage(asunto, contenido, de, para, cc=copia)
            email.send(fail_silently=False)

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
            Falla.objects.create(
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
                tipo_falla=INTEGRACION,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == MALRECHAZO:

            asunto = 'Falla Mal Rechazo' +' '+ \
            estacion.nombre +' '+ \
            actividad.banda +' '+ \
            actividad.proyecto +' '+ \
            actividad.escenario +' '+ \
            'WP:' +' '+ \
            str(actividad.wp)

            contenido = 'Buen día Andrea Guerrero' +'\n'+'\n'+ \
            conceptos.last().contenido +'\n'+'\n'+ \
            'Ingeniero Nokia: ' + ni_ingeniero.nombre_completo.title() +'\n'+'\n'+ \
            'Service Supplier: '+ service_supplier +'\n'+'\n'+ \
            'Cordial Saludo,' +'\n'+'\n'+ 'OnAir Team'

            de = 'notification_onair.noreply@gaponair.com'

            para = ['ague.workforce@nokia.com']

            copia = ['jbri.gap@nokia.com',
                    'I_EXT_GAP_CLARO_COL@nokia.com',
                    'jorge.baracaldo@nokia.com',
                    'dtor.onair_claro@nokia.com',
                    'jsan.onair_claro@nokia.com']

            email = EmailMessage(asunto, contenido, de, para, cc=copia)
            email.send(fail_silently=False)

            NotificacionFallaMalRechazo.objects.create(
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
            Falla.objects.create(
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
                tipo_falla=MALRECHAZO,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == SOFTWARE:
            Falla.objects.create(
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
                tipo_falla=SOFTWARE,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == HARDWARE:
            Falla.objects.create(
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
                tipo_falla=HARDWARE,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == DATAFILL:
            Falla.objects.create(
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
                tipo_falla=DATAFILL,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == AJUSTEPOTENCIA:
            Falla.objects.create(
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
                tipo_falla=AJUSTEPOTENCIA,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == INTERFERENCIAEXTREMA:
            Falla.objects.create(
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
                tipo_falla=INTERFERENCIAEXTREMA,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == CAMBIODISENO:
            Falla.objects.create(
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
                tipo_falla=CAMBIODISENO,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == TX:
            Falla.objects.create(
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
                tipo_falla=TX,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == COMPORTAMIENTOESPERADO:
            Falla.objects.create(
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
                tipo_falla=COMPORTAMIENTOESPERADO,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == COMPORTAMIENTOPREVIO:
            Falla.objects.create(
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
                tipo_falla=COMPORTAMIENTOPREVIO,
            )
        if estado_asignacion == ENVIADO_A_SEGUIMIENTO and origen_falla == AJUSTEADYACENCIAS:
            Falla.objects.create(
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
                tipo_falla=AJUSTEADYACENCIAS,
            )
        return cleaned_data
