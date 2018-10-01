# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
# views AsignacionNpo for CRUD
ListAsignacionNpo,
DetailAsignacionNpo,
UpdateAsignacionNpo,
UpdateAsignacionNpoAsiganador,
UpdateAsignacionNpoIngeniero,
CreateAsignacionNpo,
DeleteAsignacionNpo,
# views AsignacionNpo for queryset
SearchAsignacionNpo,
ListAsignacionNpoActividad,
ListAsignacionNpoPerfil,
ListAsignacionNpoEstadoA,
ListAsignacionNpoEstadoB,
ListAsignacionNpoEstadoC,
ListAsignacionNpoEstadoD,
ListAsignacionNpoEstadoE,
ListAsignacionNpoEstadoF,
ListAsignacionNpoEstadoG,
ListAsignacionNpoHoy,
ListAsignacionNpoFecha,
# views AsignacionNi for CRUD
ListAsignacionNi,
DetailAsignacionNi,
UpdateAsignacionNi,
UpdateAsignacionNiAsignador,
UpdateAsignacionNiIngeniero,
CreateAsignacionNi,
DeleteAsignacionNi,
# views AsignacionNi for queryset
SearchAsignacionNi,
ListAsignacionNiActividad,
ListAsignacionNiPerfil,
ListAsignacionNiEstadoA,
ListAsignacionNiEstadoB,
ListAsignacionNiEstadoC,
ListAsignacionNiEstadoD,
ListAsignacionNiEstadoE,
ListAsignacionNiEstadoF,
ListAsignacionNiEstadoG,
ListAsignacionNiHoy,
ListAsignacionNiFecha,

)
from . import views

app_name = 'asignaciones'
urlpatterns = [

    # urls AsignacionNpo for CRUD
    url(r'^list/asignacion/npo/$', ListAsignacionNpo.as_view(), name='list_asignacion_npo'),
    url(r'^create_asignacion_npo/(?P<pk>\d+)/$', CreateAsignacionNpo.as_view(), name='create_asignacion_npo'),
    url(r'^detail_asignacion_npo/(?P<pk>\d+)/$', DetailAsignacionNpo.as_view(), name='detail_asignacion_npo'),
    url(r'^update_asignacion_npo/(?P<pk>\d+)/$', UpdateAsignacionNpo.as_view(), name='update_asignacion_npo'),
    url(r'^update/asignacion/npo/asignador/(?P<pk>\d+)/$', UpdateAsignacionNpoAsiganador.as_view(),
                                            name='update_asignacion_npo_asignador'),
    url(r'^update/asignacion/npo/ingeniero/(?P<pk>\d+)/$', UpdateAsignacionNpoIngeniero.as_view(),
                                            name='update_asignacion_npo_ingeniero'),
    url(r'^delete_asignacion_npo/(?P<pk>\d+)/$', DeleteAsignacionNpo.as_view(), name='delete_asignacion_npo'),

    # urls AsignacionNpo for queryset
    url(r'^search_asignacion_npo/$', SearchAsignacionNpo.as_view(),
                                            name='search_asignacion_npo'),
    url(r'^list/asignacion/npo/actividad/(?P<pk>\d+)/$', ListAsignacionNpoActividad.as_view(),
                                            name='list_asignacion_npo_actividad'),
    url(r'^list/asignacion/npo/perfil/(?P<slug>[-\w]+)/$', ListAsignacionNpoPerfil.as_view(),
                                            name='list_asignacion_npo_perfil'),
    url(r'^list/asignacion/npo/estado/a/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoA.as_view(),
                                            name='list_asignacion_npo_estado_a'),
    url(r'^list/asignacion/npo/estado/b/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoB.as_view(),
                                            name='list_asignacion_npo_estado_b'),
    url(r'^list/asignacion/npo/estado/c/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoC.as_view(),
                                            name='list_asignacion_npo_estado_c'),
    url(r'^list/asignacion/npo/estado/d/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoD.as_view(),
                                            name='list_asignacion_npo_estado_d'),
    url(r'^list/asignacion/npo/estado/e/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoE.as_view(),
                                            name='list_asignacion_npo_estado_e'),
    url(r'^list/asignacion/npo/estado/f/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoF.as_view(),
                                            name='list_asignacion_npo_estado_f'),
    url(r'^list/asignacion/npo/estado/g/(?P<slug>[-\w]+)/$', ListAsignacionNpoEstadoG.as_view(),
                                            name='list_asignacion_npo_estado_g'),
    url(r'^list/asignacion/npo/estado/hoy/(?P<slug>[-\w]+)/$', ListAsignacionNpoHoy.as_view(),
                                            name='list_asignacion_npo_hoy'),
    url(r'^list/asignacion/npo/fecha/(?P<slug>[-\w]+)/$', ListAsignacionNpoFecha.as_view(),
                                            name='list_asignacion_npo_fecha'),

    # url AsignacionNpo for export
    url(r'^export/asignaciones/npo/$', views.export_asignaciones_npo, name='export_asignaciones_npo'),

    # urls AsignacionNi for CRUD
    url(r'^list/asignacion/ni/$', ListAsignacionNi.as_view(), name='list_asignacion_ni'),
    url(r'^create_asignacion_ni/(?P<pk>\d+)/$', CreateAsignacionNi.as_view(), name='create_asignacion_ni'),
    url(r'^detail_asignacion_ni/(?P<pk>\d+)/$', DetailAsignacionNi.as_view(), name='detail_asignacion_ni'),
    url(r'^update_asignacion_ni/(?P<pk>\d+)/$', UpdateAsignacionNi.as_view(), name='update_asignacion_ni'),
    url(r'^update/asignacion/ni/asignador/(?P<pk>\d+)/$', UpdateAsignacionNiAsignador.as_view(),
                                            name='update_asignacion_ni_asignador'),
    url(r'^update/asignacion/ni/ingeniero/(?P<pk>\d+)/$', UpdateAsignacionNiIngeniero.as_view(),
                                            name='update_asignacion_ni_ingeniero'),
    url(r'^delete_asignacion_ni/(?P<pk>\d+)/$', DeleteAsignacionNi.as_view(), name='delete_asignacion_ni'),

    # urls AsignacionNi for queryset
    url(r'^search_asignacion_ni/$', SearchAsignacionNi.as_view(),
                                            name='search_asignacion_ni'),
    url(r'^list/asignacion/ni/actividad/(?P<pk>\d+)/$', ListAsignacionNiActividad.as_view(),
                                            name='list_asignacion_ni_actividad'),
    url(r'^list/asignacion/ni/perfil/(?P<slug>[-\w]+)/$', ListAsignacionNiPerfil.as_view(),
                                            name='list_asignacion_ni_perfil'),
    url(r'^list/asignacion/ni/estado/a/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoA.as_view(),
                                            name='list_asignacion_ni_estado_a'),
    url(r'^list/asignacion/ni/estado/b/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoB.as_view(),
                                            name='list_asignacion_ni_estado_b'),
    url(r'^list/asignacion/ni/estado/c/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoC.as_view(),
                                            name='list_asignacion_ni_estado_c'),
    url(r'^list/asignacion/ni/estado/d/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoD.as_view(),
                                            name='list_asignacion_ni_estado_d'),
    url(r'^list/asignacion/ni/estado/e/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoE.as_view(),
                                            name='list_asignacion_ni_estado_e'),
    url(r'^list/asignacion/ni/estado/f/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoF.as_view(),
                                            name='list_asignacion_ni_estado_f'),
    url(r'^list/asignacion/ni/estado/g/(?P<slug>[-\w]+)/$', ListAsignacionNiEstadoG.as_view(),
                                            name='list_asignacion_ni_estado_g'),
    url(r'^list/asignacion/ni/estado/hoy/(?P<slug>[-\w]+)/$', ListAsignacionNiHoy.as_view(),
                                            name='list_asignacion_ni_hoy'),
    url(r'^list/asignacion/ni/fecha/(?P<slug>[-\w]+)/$', ListAsignacionNiFecha.as_view(),
                                            name='list_asignacion_ni_fecha'),

    # url AsignacionNi for export
    url(r'^export/asignaciones/ni/$', views.export_asignaciones_ni, name='export_asignaciones_ni'),

]
