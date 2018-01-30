# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
ListNotificacionRequiereVisita,
SearchNotificacionRequiereVisita,
ListNotificacionFallaInstalacion,
SearchNotificacionFallaInstalacion,
ListNotificacionFallaIntegracion,
SearchNotificacionFallaIntegracion,
ListNotificacionFallaSoftware,
SearchNotificacionFallaSoftware,
ListNotificacionFallaHardware,
SearchNotificacionFallaHardware,
ListNotificacionFallaDatafill,
SearchNotificacionFallaDatafill,
ListNotificacionFallaAjustePotencia,
SearchNotificacionFallaAjustePotencia,
ListNotificacionFallaInterferenciaExterna,
SearchNotificacionFallaInterferenciaExterna,
ListNotificacionFallaCambioDiseno,
SearchNotificacionFallaCambioDiseno,
ListNotificacionFallaMalRechazo,
SearchNotificacionFallaMalRechazo,
ListNotificacionFallaTX,
SearchNotificacionFallaTX,
ListNotificacionFallaComportamientoEsperado,
SearchNotificacionFallaComportamientoEsperado,
)
from . import views

app_name = 'notificaciones'
urlpatterns = [
    url(r'^list/notificacion/requiere_visita/$', ListNotificacionRequiereVisita.as_view(), name='list_notificacion_requiere_visita'),
    url(r'^search/notificacion/requiere_visita/$', SearchNotificacionRequiereVisita.as_view(), name='search_notificacion_requiere_visita'),
    url(r'^export/notificaciones/requiere_visita/$', views.export_notificaciones_requiere_visita, name='export_notificaciones_requiere_visita'),

    url(r'^list/notificacion/falla_instalacion/$', ListNotificacionFallaInstalacion.as_view(), name='list_notificacion_falla_instalacion'),
    url(r'^search/notificacion/falla_instalacion/$', SearchNotificacionFallaInstalacion.as_view(), name='search_notificacion_falla_instalacion'),
    url(r'^export/notificaciones/falla_instalacion/$', views.export_notificaciones_falla_instalacion, name='export_notificaciones_falla_instalacion'),

    url(r'^list/notificacion/falla_integracion/$', ListNotificacionFallaIntegracion.as_view(), name='list_notificacion_falla_integracion'),
    url(r'^search/notificacion/falla_integracion/$', SearchNotificacionFallaIntegracion.as_view(), name='search_notificacion_falla_integracion'),
    url(r'^export/notificaciones/falla_integracion/$', views.export_notificaciones_falla_integracion, name='export_notificaciones_falla_integracion'),

    url(r'^list/notificacion/falla_software/$', ListNotificacionFallaSoftware.as_view(), name='list_notificacion_falla_software'),
    url(r'^search/notificacion/falla_software/$', SearchNotificacionFallaSoftware.as_view(), name='search_notificacion_falla_software'),
    url(r'^export/notificaciones/falla_software/$', views.export_notificaciones_falla_software, name='export_notificaciones_falla_software'),

    url(r'^list/notificacion/falla_hardware/$', ListNotificacionFallaHardware.as_view(), name='list_notificacion_falla_hardware'),
    url(r'^search/notificacion/falla_hardware/$', SearchNotificacionFallaHardware.as_view(), name='search_notificacion_falla_hardware'),
    url(r'^export/notificaciones/falla_hardware/$', views.export_notificaciones_falla_hardware, name='export_notificaciones_falla_hardware'),

    url(r'^list/notificacion/falla_datafill/$', ListNotificacionFallaDatafill.as_view(), name='list_notificacion_falla_datafill'),
    url(r'^search/notificacion/falla_datafill/$', SearchNotificacionFallaDatafill.as_view(), name='search_notificacion_falla_datafill'),
    url(r'^export/notificaciones/falla_datafill/$', views.export_notificaciones_falla_datafill, name='export_notificaciones_falla_datafill'),

    url(r'^list/notificacion/falla_ajuste_potencia/$', ListNotificacionFallaAjustePotencia.as_view(), name='list_notificacion_falla_ajuste_potencia'),
    url(r'^search/notificacion/falla_ajuste_potencia/$', SearchNotificacionFallaAjustePotencia.as_view(), name='search_notificacion_falla_ajuste_potencia'),
    url(r'^export/notificaciones/falla_ajuste_potencia/$', views.export_notificaciones_falla_ajuste_potencia, name='export_notificaciones_falla_ajuste_potencia'),

    url(r'^list/notificacion/falla_interferencia_externa/$', ListNotificacionFallaInterferenciaExterna.as_view(), name='list_notificacion_falla_interferencia_externa'),
    url(r'^search/notificacion/falla_interferencia_externa/$', SearchNotificacionFallaInterferenciaExterna.as_view(), name='search_notificacion_falla_interferencia_externa'),
    url(r'^export/notificaciones/falla_interferencia_externa/$', views.export_notificaciones_falla_interferencia_externa, name='export_notificaciones_falla_interferencia_externa'),

    url(r'^list/notificacion/falla_cambio_diseno/$', ListNotificacionFallaCambioDiseno.as_view(), name='list_notificacion_falla_cambio_diseno'),
    url(r'^search/notificacion/falla_cambio_diseno/$', SearchNotificacionFallaCambioDiseno.as_view(), name='search_notificacion_falla_cambio_diseno'),
    url(r'^export/notificaciones/falla_cambio_diseno/$', views.export_notificaciones_falla_cambio_diseno, name='export_notificaciones_falla_cambio_diseno'),

    url(r'^list/notificacion/falla_mal_rechazo/$', ListNotificacionFallaMalRechazo.as_view(), name='list_notificacion_falla_mal_rechazo'),
    url(r'^search/notificacion/falla_mal_rechazo/$', SearchNotificacionFallaMalRechazo.as_view(), name='search_notificacion_falla_mal_rechazo'),
    url(r'^export/notificaciones/falla_mal_rechazo/$', views.export_notificaciones_falla_mal_rechazo, name='export_notificaciones_falla_mal_rechazo'),

    url(r'^list/notificacion/falla_tx/$', ListNotificacionFallaTX.as_view(), name='list_notificacion_falla_tx'),
    url(r'^search/notificacion/falla_tx/$', SearchNotificacionFallaTX.as_view(), name='search_notificacion_falla_tx'),
    url(r'^export/notificaciones/falla_tx/$', views.export_notificaciones_falla_tx, name='export_notificaciones_falla_tx'),

    url(r'^list/notificacion/falla_comportamiento_esperado/$', ListNotificacionFallaComportamientoEsperado.as_view(), name='list_notificacion_falla_comportamiento_esperado'),
    url(r'^search/notificacion/falla_comportamiento_esperado/$', SearchNotificacionFallaComportamientoEsperado.as_view(), name='search_notificacion_falla_comportamiento_esperado'),
    url(r'^export/notificaciones/falla_comportamiento_esperado/$', views.export_notificaciones_falla_comportamiento_esperado, name='export_notificaciones_falla_comportamiento_esperado'),
]
