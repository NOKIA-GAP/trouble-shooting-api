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
ListNotificacionFallaMalRechazo,
SearchNotificacionFallaMalRechazo,
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

    url(r'^list/notificacion/falla_mal_rechazo/$', ListNotificacionFallaMalRechazo.as_view(), name='list_notificacion_falla_mal_rechazo'),
    url(r'^search/notificacion/falla_mal_rechazo/$', SearchNotificacionFallaMalRechazo.as_view(), name='search_notificacion_falla_mal_rechazo'),
    url(r'^export/notificaciones/falla_mal_rechazo/$', views.export_notificaciones_falla_mal_rechazo, name='export_notificaciones_falla_mal_rechazo'),
]
