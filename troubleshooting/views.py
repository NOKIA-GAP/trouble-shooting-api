# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from estaciones.panels import (
estaciones,
estaciones_estado_produccion,
estaciones_estado_enviado_a_seguimiento,
estaciones_estado_escalado_a_claro,
estaciones_estado_en_monitoreo,
estaciones_estado_requiere_visita,
estaciones_estado_asignada,
estaciones_estado_none,
)
from actividades.panels import (
actividades,
actividades_estado_noc_produccion,
actividades_estado_noc_seguimiento_12h,
actividades_estado_noc_seguimiento_24h,
actividades_estado_noc_seguimiento_36h,
actividades_estado_noc_escalado_a_implementacion,
actividades_estado_noc_escalado_a_grupo_calidad,
actividades_estado_noc_escalado_a_rf,
actividades_estado_noc_escalado_a_oym,
actividades_estado_noc_escalado_a_gdrt,
actividades_estado_noc_escalado_control_cambios,
actividades_estado_noc_precheck,
actividades_estado_noc_pendiente_remedy,
actividades_estado_noc_stand_by,
actividades_estado_noc_rollback,
actividades_estado_noc_suspendido,
actividades_estado_noc_none,
)
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
from incidentes.panels import (
incidentes_npo,
incidentes_npo_abierto,
incidentes_npo_cerrado,
incidentes_ni,
incidentes_ni_abierto,
incidentes_ni_cerrado,
)
from solicitudeshw.panels import (
solicitudeshw,
solicitudeshw_hwrequrido,
solicitudeshw_hwsolicitado,
solicitudeshw_hwrecibido,
solicitudeshw_hwcancelado,
)
from notificaciones.panels import (
notificaciones_requiere_visita,
notificacion_falla_instalacion,
notificacion_falla_integracion,
notificacion_falla_software,
notificacion_falla_hardware,
notificacion_falla_datafill,
notificacion_falla_ajuste_potencia,
notificacion_falla_interferencia_externa,
notificacion_falla_cambio_diseno,
notificacion_falla_mal_rechazo,
notificacion_falla_tx,
notificacion_falla_comportamiento_esperado,
notificacion_falla_comportamiento_previo,
)
from asignaciones.models import (
AsignacionNpo,
AsignacionNi,
)
import datetime

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'

TODAY = datetime.date.today()
YESTERDAY = datetime.date.today() - datetime.timedelta(1)
THREEDAYS = datetime.date.today() - datetime.timedelta(3)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # estaciones
        context['estaciones'] = estaciones.count()
        context['estaciones_estado_produccion'] = estaciones_estado_produccion.count()
        context['estaciones_estado_enviado_a_seguimiento'] = estaciones_estado_enviado_a_seguimiento.count()
        context['estaciones_estado_escalado_a_claro'] = estaciones_estado_escalado_a_claro.count()
        context['estaciones_estado_en_monitoreo'] = estaciones_estado_en_monitoreo.count()
        context['estaciones_estado_requiere_visita'] = estaciones_estado_requiere_visita.count()
        context['estaciones_estado_asignada'] = estaciones_estado_asignada.count()
        context['estaciones_estado_none'] = estaciones_estado_none.count()
        # actividades
        context['actividades'] = actividades.count()
        context['actividades_estado_noc_produccion'] = actividades_estado_noc_produccion.count()
        context['actividades_estado_noc_seguimiento_12h'] = actividades_estado_noc_seguimiento_12h.count()
        context['actividades_estado_noc_seguimiento_24h'] = actividades_estado_noc_seguimiento_24h.count()
        context['actividades_estado_noc_seguimiento_36h'] = actividades_estado_noc_seguimiento_36h.count()
        context['actividades_estado_noc_escalado_a_implementacion'] = actividades_estado_noc_escalado_a_implementacion.count()
        context['actividades_estado_noc_escalado_a_grupo_calidad'] = actividades_estado_noc_escalado_a_grupo_calidad.count()
        context['actividades_estado_noc_escalado_a_rf'] = actividades_estado_noc_escalado_a_rf.count()
        context['actividades_estado_noc_escalado_a_oym'] = actividades_estado_noc_escalado_a_oym.count()
        context['actividades_estado_noc_escalado_a_gdrt'] = actividades_estado_noc_escalado_a_gdrt.count()
        context['actividades_estado_noc_escalado_control_cambios'] = actividades_estado_noc_escalado_control_cambios.count()
        context['actividades_estado_noc_precheck'] = actividades_estado_noc_precheck.count()
        context['actividades_estado_noc_pendiente_remedy'] = actividades_estado_noc_pendiente_remedy.count()
        context['actividades_estado_noc_stand_by'] = actividades_estado_noc_stand_by.count()
        context['actividades_estado_noc_rollback'] = actividades_estado_noc_rollback.count()
        context['actividades_estado_noc_suspendido'] = actividades_estado_noc_suspendido.count()
        context['actividades_estado_noc_none'] = actividades_estado_noc_none.count()

        # asignaciones npo
        context['asignaciones_npo'] = asignaciones_npo.count()
        context['asignaciones_npo_asignada'] = asignaciones_npo_asignada.count()
        context['asignaciones_npo_requiere_visita'] = asignaciones_npo_requiere_visita.count()
        context['asignaciones_npo_en_monitoreo'] = asignaciones_npo_en_monitoreo.count()
        context['asignaciones_npo_escalado_a_claro'] = asignaciones_npo_escalado_a_claro.count()
        context['asignaciones_npo_enviado_a_seguimiento'] = asignaciones_npo_enviado_a_seguimiento.count()

        context['asignaciones_npo_asignada_un_dia'] = asignaciones_npo_asignada_un_dia.count()
        context['asignaciones_npo_en_monitoreo_tres_dias'] = asignaciones_npo_en_monitoreo_tres_dias.count()

        # asignaciones ni
        context['asignaciones_ni'] = asignaciones_ni.count()
        context['asignaciones_ni_asignada'] = asignaciones_ni_asignada.count()
        context['asignaciones_ni_requiere_visita'] = asignaciones_ni_requiere_visita.count()
        context['asignaciones_ni_en_monitoreo'] = asignaciones_ni_en_monitoreo.count()
        context['asignaciones_ni_escalado_a_claro'] = asignaciones_ni_escalado_a_claro.count()
        context['asignaciones_ni_enviado_a_seguimiento'] = asignaciones_ni_enviado_a_seguimiento.count()

        context['asignaciones_ni_asignada_un_dia'] = asignaciones_ni_asignada_un_dia.count()
        context['asignaciones_ni_en_monitoreo_tres_dias'] = asignaciones_ni_en_monitoreo_tres_dias.count()

        # incidentes npo
        context['incidentes_npo'] = incidentes_npo.count()
        context['incidentes_npo_abierto'] = incidentes_npo_abierto.count()
        context['incidentes_npo_cerrado'] = incidentes_npo_cerrado.count()

        # incidentes ni
        context['incidentes_ni'] = incidentes_ni.count()
        context['incidentes_ni_abierto'] = incidentes_ni_abierto.count()
        context['incidentes_ni_cerrado'] = incidentes_ni_cerrado.count()

        # solicitudeshw
        context['solicitudeshw'] = solicitudeshw.count()
        context['solicitudeshw_hwrequrido'] = solicitudeshw_hwrequrido.count()
        context['solicitudeshw_hwsolicitado'] = solicitudeshw_hwsolicitado.count()
        context['solicitudeshw_hwrecibido'] = solicitudeshw_hwrecibido.count()
        context['solicitudeshw_hwcancelado'] = solicitudeshw_hwcancelado.count()

        # notificaciones
        context['notificaciones_requiere_visita'] = notificaciones_requiere_visita.count()
        context['notificacion_falla_instalacion'] = notificacion_falla_instalacion.count()
        context['notificacion_falla_integracion'] = notificacion_falla_integracion.count()
        context['notificacion_falla_software'] = notificacion_falla_software.count()
        context['notificacion_falla_hardware'] = notificacion_falla_hardware.count()
        context['notificacion_falla_datafill'] = notificacion_falla_datafill.count()
        context['notificacion_falla_ajuste_potencia'] = notificacion_falla_ajuste_potencia.count()
        context['notificacion_falla_interferencia_externa'] = notificacion_falla_interferencia_externa.count()
        context['notificacion_falla_cambio_diseno'] = notificacion_falla_cambio_diseno.count()
        context['notificacion_falla_mal_rechazo'] = notificacion_falla_mal_rechazo.count()
        context['notificacion_falla_tx'] = notificacion_falla_tx.count()
        context['notificacion_falla_comportamiento_esperado'] = notificacion_falla_comportamiento_esperado.count()
        context['notificacion_falla_comportamiento_previo'] = notificacion_falla_comportamiento_previo.count()

        return context
