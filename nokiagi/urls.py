from django.conf.urls import url
from .views import (
ListGi,
# SearchFalla,
)
from . import views

app_name = 'nokiagi'
urlpatterns = [
    url(r'^list/gi/$', ListGi.as_view(), name='list_gi'),
    # url(r'^search/falla/$', SearchFalla.as_view(), name='search_falla'),
    # url(r'^export/fallas/$', views.export_fallas, name='export_fallas'),
    url(r'^actualizacion/$', views.actualizacion, name='actualizacion'),
    url(r'^creacion/$', views.creacion, name='creacion'),
]
