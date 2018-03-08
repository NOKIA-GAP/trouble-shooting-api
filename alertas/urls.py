from django.conf.urls import url
from .views import (
ListAlerta,
DetailAlerta,
UpdateAlerta,
DeleteAlerta,
SearchAlerta,
)
from . import views

app_name = 'alertas'
urlpatterns = [
    url(r'^list/alerta$', ListAlerta.as_view(), name='list_alerta'),
    url(r'^detail/alerta/(?P<pk>\d+)/$', DetailAlerta.as_view(), name='detail_alerta'),
    url(r'^update/alerta/(?P<pk>\d+)/$', UpdateAlerta.as_view(), name='update_alerta'),
    url(r'^delete/alerta/(?P<pk>\d+)/$', DeleteAlerta.as_view(), name='delete_alerta'),
    url(r'^search/alerta/$', SearchAlerta.as_view(), name='search_alerta'),
]
