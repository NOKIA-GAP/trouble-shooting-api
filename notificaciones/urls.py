# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

app_name = 'notificaciones'
urlpatterns = [
    url(r'^export/notificaciones/requiere_visita/$', views.export_notificaciones_requiere_visita, name='export_notificaciones_requiere_visita'),
    url(r'^export/notificaciones/falla_instalacion/$', views.export_notificaciones_falla_instalacion, name='export_notificaciones_falla_instalacion'),
    url(r'^export/notificaciones/falla_integracion/$', views.export_notificaciones_falla_integracion, name='export_notificaciones_falla_integracion'),
]
