from django.conf.urls import url
from .views import (
ListGi,
SearchGi,
FilterGi,
)
from . import views

app_name = 'nokiagi'
urlpatterns = [
    url(r'^list/gi/$', ListGi.as_view(), name='list_gi'),
    url(r'^search/gi/$', SearchGi.as_view(), name='search_gi'),
    url(r'^filter/gi/$', FilterGi.as_view(), name='filter_gi'),
    # url(r'^export/fallas/$', views.export_fallas, name='export_fallas'),
    url(r'^actualizacion/$', views.actualizacion, name='actualizacion'),
    url(r'^creacion/$', views.creacion, name='creacion'),
    url(r'^normalizacion/$', views.normalizacion, name='normalizacion'),
]
