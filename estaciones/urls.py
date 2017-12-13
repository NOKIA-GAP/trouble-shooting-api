from django.conf.urls import url
from .views import (
ListEstacion,
DetailEstacion,
UpdateEstacion,
CreateEstacion,
DeleteEstacion,
SearchEstacion,
FilterEstacion,
)
from . import views

app_name = 'estaciones'
urlpatterns = [
    url(r'^list_estacion/$', ListEstacion.as_view(), name='list_estacion'),
    url(r'^create_estacion/$', CreateEstacion.as_view(), name='create_estacion'),
    url(r'^detail_estacion/(?P<pk>\d+)/$', DetailEstacion.as_view(), name='detail_estacion'),
    url(r'^update_estacion/(?P<pk>\d+)/$', UpdateEstacion.as_view(), name='update_estacion'),
    url(r'^delete_estacion/(?P<pk>\d+)/$', DeleteEstacion.as_view(), name='delete_estacion'),
    url(r'^search_estacion/$', SearchEstacion.as_view(), name='search_estacion'),
    url(r'^filter/estacion/$', FilterEstacion.as_view(), name='filter_estacion'),
    url(r'^export_estaciones/$', views.export_estaciones, name='export_estaciones'),
]
