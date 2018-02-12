# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from estaciones.models import Estacion
from actividades.models import Actividad
from asignaciones.models import AsignacionNpo, AsignacionNi
from asignaciones.panels import (
asignaciones_npo,
asignaciones_ni,
asignaciones_npo_asignada,
asignaciones_npo_requiere_visita,
asignaciones_npo_en_monitoreo,
asignaciones_npo_escalado_a_claro,
asignaciones_npo_enviado_a_seguimiento,

asignaciones_npo_asignada_un_dia,
asignaciones_npo_en_monitoreo_tres_dias,

asignaciones_ni_asignada,
asignaciones_ni_requiere_visita,
asignaciones_ni_en_monitoreo,
asignaciones_ni_escalado_a_claro,
asignaciones_ni_enviado_a_seguimiento,

asignaciones_ni_asignada_un_dia,
asignaciones_ni_en_monitoreo_tres_dias,
)
from incidentes.models import IncidenteNpo, IncidenteNi
from solicitudeshw.models import SolicitudHW

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
PRODUCCION = 'Produccion'
ABIERTO = 'Abierto'
CERRADO = 'Cerrado'
REQUIEREHW = 'Requiere HW'
HWSOLICITADO = 'HW solicitado'
HWRECIBIDO = 'HW recibido'
CANCELADA = 'Cancelada'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # estaciones
        context['estaciones'] = Estacion.objects.all().count()
        context['estaciones_estado_produccion'] = Estacion.objects.filter(estado_estacion=PRODUCCION).count()
        context['estaciones_estado_enviado_a_seguimiento'] = Estacion.objects.filter(estado_estacion=ENVIADO_A_SEGUIMIENTO).count()
        context['estaciones_estado_escalado_a_claro'] = Estacion.objects.filter(estado_estacion=ESCALADO_A_CLARO).count()
        context['estaciones_estado_en_monitoreo'] = Estacion.objects.filter(estado_estacion=EN_MONITOREO).count()
        context['estaciones_estado_requiere_visita'] = Estacion.objects.filter(estado_estacion=REQUIERE_VISITA).count()
        context['estaciones_estado_asignada'] = Estacion.objects.filter(estado_estacion=ASIGNADA).count()
        # actividades
        context['actividades'] = Actividad.objects.all().count()
        context['actividades_estado_noc_produccion'] = Actividad.objects.filter(estado_noc=PRODUCCION).count()

        # asignaciones npo
        context['asignaciones_npo'] = asignaciones_npo
        context['asignaciones_npo_asignada'] = asignaciones_npo_asignada
        context['asignaciones_npo_requiere_visita'] = asignaciones_npo_requiere_visita
        context['asignaciones_npo_en_monitoreo'] = asignaciones_npo_en_monitoreo
        context['asignaciones_npo_escalado_a_claro'] = asignaciones_npo_escalado_a_claro
        context['asignaciones_npo_enviado_a_seguimiento'] = asignaciones_npo_enviado_a_seguimiento

        context['asignaciones_npo_asignada_un_dia'] = asignaciones_npo_asignada_un_dia
        context['asignaciones_npo_en_monitoreo_tres_dias'] = asignaciones_npo_en_monitoreo_tres_dias

        # asignaciones ni
        context['asignaciones_ni'] = asignaciones_ni
        context['asignaciones_ni_asignada'] = asignaciones_ni_asignada
        context['asignaciones_ni_requiere_visita'] = asignaciones_ni_requiere_visita
        context['asignaciones_ni_en_monitoreo'] = asignaciones_ni_en_monitoreo
        context['asignaciones_ni_escalado_a_claro'] = asignaciones_ni_escalado_a_claro
        context['asignaciones_ni_enviado_a_seguimiento'] = asignaciones_ni_enviado_a_seguimiento

        context['asignaciones_ni_asignada_un_dia'] = asignaciones_ni_asignada_un_dia
        context['asignaciones_ni_en_monitoreo_tres_dias'] = asignaciones_ni_en_monitoreo_tres_dias

        # incidentes npo
        context['incidentes_npo'] = IncidenteNpo.objects.all().count()
        context['incidentes_npo_abierto'] = IncidenteNpo.objects.filter(estado_incidente=ABIERTO).count()
        context['incidentes_npo_cerrado'] = IncidenteNpo.objects.filter(estado_incidente=CERRADO).count()

        # incidentes ni
        context['incidentes_ni'] = IncidenteNi.objects.all().count()
        context['incidentes_ni_abierto'] = IncidenteNi.objects.filter(estado_incidente=ABIERTO).count()
        context['incidentes_ni_cerrado'] = IncidenteNi.objects.filter(estado_incidente=CERRADO).count()

        # solicitudeshw
        context['solicitudeshw'] = SolicitudHW.objects.all().count()
        context['solicitudeshw_hwrequrido'] = SolicitudHW.objects.filter(estado_solicitud=REQUIEREHW).count()
        context['solicitudeshw_hwsolicitado'] = SolicitudHW.objects.filter(estado_solicitud=HWSOLICITADO).count()
        context['solicitudeshw_hwrecibido'] = SolicitudHW.objects.filter(estado_solicitud=HWRECIBIDO).count()
        context['solicitudeshw_hwcancelado'] = SolicitudHW.objects.filter(estado_solicitud=CANCELADA).count()

        return context
