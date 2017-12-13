# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
# views SolicitudHW for CRUD
ListSolicitudHW,
DetailSolicitudHW,
CreateSolicitudHW,
UpdateSolicitudHW,
DeleteSolicitudHW,
# views SolicitudHW for queryset
SearchSolicitudHW,
ListSolicitudHWActividad,
ListSolicitudHWAsignacion,
# views SolicitudHW for CRUD
ListSolicitud,
DetailSolicitud,
# CreateSolicitud,
UpdateSolicitud,
DeleteSolicitud,
# views SolicitudHW for queryset
ListSolicitudSolicitudHW,
)
from . import views

app_name = 'solicitudeshw'
urlpatterns = [

    # urls SolicitudHW for CRUD
    url(r'^list/solicitudhw$', ListSolicitudHW.as_view(), name='list_solicitudhw'),
    url(r'^create/solicitudhw/(?P<pk>\d+)/$', CreateSolicitudHW.as_view(), name='create_solicitudhw'),
    url(r'^detail/solicitudhw/(?P<pk>\d+)/$', DetailSolicitudHW.as_view(), name='detail_solicitudhw'),
    url(r'^update/solicitudhw/(?P<pk>\d+)/$', UpdateSolicitudHW.as_view(), name='update_solicitudhw'),
    url(r'^delete/solicitudhw/(?P<pk>\d+)/$', DeleteSolicitudHW.as_view(), name='delete_solicitudhw'),

    # urls SolicitudHW for queryset
    url(r'^search/solicitudhw$', SearchSolicitudHW.as_view(),
                                            name='search_solicitudhw'),
    url(r'^list/solicitudhw/actividad/(?P<pk>\d+)/$', ListSolicitudHWActividad.as_view(),
                                            name='list_solicitudhw_actividad'),
    url(r'^list/solicitudhw/asignacion/(?P<pk>\d+)/$', ListSolicitudHWAsignacion.as_view(),
                                            name='list_solicitudhw_asignacion'),

    # url SolicitudHW for export
    url(r'^export/solicitudeshw$', views.export_solicitudeshw, name='export_solicitudeshw'),

    # urls Solicitud for CRUD
    url(r'^list/solicitud$', ListSolicitud.as_view(), name='list_solicitud'),
    # url(r'^create/solicitud/(?P<pk>\d+)/$', CreateSolicitud.as_view(), name='create_solicitud'),
    url(r'^detail/solicitud/(?P<pk>\d+)/$', DetailSolicitud.as_view(), name='detail_solicitud'),
    url(r'^update/solicitud/(?P<pk>\d+)/$', UpdateSolicitud.as_view(), name='update_solicitud'),
    url(r'^delete/solicitud/(?P<pk>\d+)/$', DeleteSolicitud.as_view(), name='delete_solicitud'),
    # urls Solicitud for queryset
    url(r'^list/solicitud/solicitudhw/(?P<pk>\d+)/$', ListSolicitudSolicitudHW.as_view(),
                                            name='list_solicitud_solicitudhw'),
]
