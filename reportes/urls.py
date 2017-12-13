# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import ListReporteActividad, CreateReporteActividad, DetailReporteActividad
from . import views

app_name = 'reportes'
urlpatterns = [

    # urls ReporteActividad for CRUD
    url(r'^list/reporte_actividad/$', ListReporteActividad.as_view(), name='list_reporte_actividad'),
    url(r'^create/reporte/actividad/$', CreateReporteActividad.as_view(), name='create_reporte_actividad'),
    url(r'^detail_reporte_actividad/(?P<pk>\d+)/$', DetailReporteActividad.as_view(), name='detail_reporte_actividad'),
    # url(r'^update_reporte_actividad/(?P<pk>\d+)/$', UpdateReporteActividad.as_view(), name='update_reporte_actividad'),
    # url(r'^delete_reporte_actividad/(?P<pk>\d+)/$', DeleteReporteActividad.as_view(), name='delete_reporte_actividad'),
    url(r'^export_reporte_actividad/$', views.export_reporte_actividad, name='export_reporte_actividad'),

]
