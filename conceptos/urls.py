# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
# views ConceptoNpo for CRUD
ListConceptoNpo,
DetailConceptoNpo,
UpdateConceptoNpo,
CreateConceptoNpo,
DeleteConceptoNpo,
# views ConceptoNpo for queryset
SearchConceptoNpo,
ListConceptoNpoActividad,
ListConceptoNpoAsignacion,
# views ConceptoNi for CRUD
ListConceptoNi,
DetailConceptoNi,
UpdateConceptoNi,
CreateConceptoNi,
DeleteConceptoNi,
# views ConceptoNpo for queryset
SearchConceptoNi,
ListConceptoNiActividad,
ListConceptoNiAsignacion,

)
from . import views

app_name = 'conceptos'
urlpatterns = [

    # urls ConceptoNpo for CRUD
    url(r'^list/concepto/npo/$', ListConceptoNpo.as_view(), name='list_concepto_npo'),
    url(r'^create/concepto/npo/(?P<pk>\d+)/$', CreateConceptoNpo.as_view(), name='create_concepto_npo'),
    url(r'^detail/concepto/npo/(?P<pk>\d+)/$', DetailConceptoNpo.as_view(), name='detail_concepto_npo'),
    url(r'^update/concepto/npo/(?P<pk>\d+)/$', UpdateConceptoNpo.as_view(), name='update_concepto_npo'),
    url(r'^delete/concepto/npo/(?P<pk>\d+)/$', DeleteConceptoNpo.as_view(), name='delete_concepto_npo'),

    # urls ConceptoNpo for queryset
    url(r'^search/concepto/npo/$', SearchConceptoNpo.as_view(),
                                            name='search_concepto_npo'),
    url(r'^list/concepto/npo/actividad/(?P<pk>\d+)/$', ListConceptoNpoActividad.as_view(),
                                            name='list_concepto_npo_actividad'),
    url(r'^list/concepto/npo/asignacion/(?P<pk>\d+)/$', ListConceptoNpoAsignacion.as_view(),
                                            name='list_concepto_npo_asignacion'),

    # url ConceptoNpo for export
    url(r'^export/conceptos/npo/$', views.export_conceptos_npo, name='export_conceptos_npo'),

    # urls ConceptoNpo for CRUD
    url(r'^list/concepto/ni/$', ListConceptoNi.as_view(), name='list_concepto_ni'),
    url(r'^create/concepto/ni/(?P<pk>\d+)/$', CreateConceptoNi.as_view(), name='create_concepto_ni'),
    url(r'^detail/concepto/ni/(?P<pk>\d+)/$', DetailConceptoNi.as_view(), name='detail_concepto_ni'),
    url(r'^update/concepto/ni/(?P<pk>\d+)/$', UpdateConceptoNi.as_view(), name='update_concepto_ni'),
    url(r'^delete/concepto/ni/(?P<pk>\d+)/$', DeleteConceptoNi.as_view(), name='delete_concepto_ni'),

    # urls ConceptoNpo for queryset
    url(r'^search/concepto/ni/$', SearchConceptoNi.as_view(),
                                            name='search_concepto_ni'),
    url(r'^list/concepto/ni/actividad/(?P<pk>\d+)/$', ListConceptoNiActividad.as_view(),
                                            name='list_concepto_ni_actividad'),
    url(r'^list/concepto/ni/asignacion/(?P<pk>\d+)/$', ListConceptoNiAsignacion.as_view(),
                                            name='list_concepto_ni_asignacion'),

    # url ConceptoNpo for export
    url(r'^export/conceptos/ni/$', views.export_conceptos_ni, name='export_conceptos_ni'),
]
