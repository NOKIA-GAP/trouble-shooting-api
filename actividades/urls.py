from django.conf.urls import url
from .views import (

ListActividad,
DetailActividad,
UpdateActividad,
CreateActividad,
DeleteActividad,
SearchActividad,
FilterActividad,

ListDegradacion,
ListDegradacionActividad,
DetailDegradacion,
UpdateDegradacion,
CreateDegradacion,
DeleteDegradacion,
SearchDegradacion,

)
from . import views

app_name = 'actividades'
urlpatterns = [

    url(r'^list/actividad/$', ListActividad.as_view(), name='list_actividad'),
    url(r'^create/actividad/$', CreateActividad.as_view(), name='create_actividad'),
    url(r'^detail/actividad/(?P<pk>\d+)/$', DetailActividad.as_view(), name='detail_actividad'),
    url(r'^update/actividad/(?P<pk>\d+)/$', UpdateActividad.as_view(), name='update_actividad'),
    url(r'^delete/actividad/(?P<pk>\d+)/$', DeleteActividad.as_view(), name='delete_actividad'),
    url(r'^search/actividad/$', SearchActividad.as_view(), name='search_actividad'),
    url(r'^filter/actividad/$', FilterActividad.as_view(), name='filter_actividad'),
    url(r'^export/actividades/$', views.export_actividades, name='export_actividades'),

    url(r'^list/degradacion/$', ListDegradacion.as_view(), name='list_degradacion'),
    url(r'^list/degradacion/actividad/(?P<pk>\d+)/$', ListDegradacionActividad.as_view(),
                                                           name='list_degradacion_actividad'),
    url(r'^create/degradacion/(?P<pk>\d+)/$', CreateDegradacion.as_view(), name='create_degradacion'),
    url(r'^detail/degradacion/(?P<pk>\d+)/$', DetailDegradacion.as_view(), name='detail_degradacion'),
    url(r'^update/degradacion/(?P<pk>\d+)/$', UpdateDegradacion.as_view(), name='update_degradacion'),
    url(r'^delete/degradacion/(?P<pk>\d+)/$', DeleteDegradacion.as_view(), name='delete_degradacion'),
    url(r'^search/degradacion/$', SearchDegradacion.as_view(), name='search_degradacion'),
    url(r'^export/degradaciones/$', views.export_degradaciones, name='export_degradaciones'),
]
