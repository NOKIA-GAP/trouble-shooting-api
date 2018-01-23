from django.conf.urls import url
from .views import (
# views IncidenteNpo for CRUD
CreateIncidenteNpo,
ListIncidenteNpo,
ListIncidenteCerradoNpo,
SearchIncidenteNpo,
DetailIncidenteNpo,
UpdateIncidenteNpo,
UpdateIncidenteIngenieroNpo,
# views IncidenteNi for CRUD
CreateIncidenteNi,
ListIncidenteNi,
ListIncidenteCerradoNi,
SearchIncidenteNi,
DetailIncidenteNi,
UpdateIncidenteNi,
UpdateIncidenteIngenieroNi,
)
from . import views

app_name = 'incidentes'
urlpatterns = [

    # urls IncidenteNpo for CRUD
    url(r'^list/incidente/npo/$', ListIncidenteNpo.as_view(), name='list_incidente_npo'),
    url(r'^list/incidente/cerrado/npo/$', ListIncidenteCerradoNpo.as_view(), name='list_incidente_cerrado_npo'),
    url(r'^create/incidente/npo/(?P<pk>\d+)/$', CreateIncidenteNpo.as_view(), name='create_incidente_npo'),
    url(r'^detail/incidente/npo/(?P<pk>\d+)/$', DetailIncidenteNpo.as_view(), name='detail_incidente_npo'),
    url(r'^update/incidente/npo/(?P<pk>\d+)/$', UpdateIncidenteNpo.as_view(), name='update_incidente_npo'),
    url(r'^update/incidente/ingeniero/npo/(?P<pk>\d+)/$', UpdateIncidenteIngenieroNpo.as_view(),
                                                                              name='update_incidente_ingeniero_npo'),
    url(r'^search/incidente/npo/$', SearchIncidenteNpo.as_view(),
                                            name='search_incidente_npo'),

    # urls IncidenteNi for CRUD
    url(r'^list/incidente/ni/$', ListIncidenteNi.as_view(), name='list_incidente_ni'),
    url(r'^list/incidente/cerrado/ni/$', ListIncidenteCerradoNi.as_view(), name='list_incidente_cerrado_ni'),
    url(r'^create/incidente/ni/(?P<pk>\d+)/$', CreateIncidenteNi.as_view(), name='create_incidente_ni'),
    url(r'^detail/incidente/ni/(?P<pk>\d+)/$', DetailIncidenteNi.as_view(), name='detail_incidente_ni'),
    url(r'^update/incidente/ni/(?P<pk>\d+)/$', UpdateIncidenteNi.as_view(), name='update_incidente_ni'),
    url(r'^update/incidente/ingeniero/ni/(?P<pk>\d+)/$', UpdateIncidenteIngenieroNi.as_view(),
                                                                              name='update_incidente_ingeniero_ni'),

    url(r'^search/incidente/ni/$', SearchIncidenteNi.as_view(),
                                            name='search_incidente_ni'),
]
