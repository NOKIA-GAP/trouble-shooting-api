# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
ListFalla,
SearchFalla,
)
from . import views

app_name = 'fallas'
urlpatterns = [
    url(r'^list/falla/$', ListFalla.as_view(), name='list_falla'),
    url(r'^search/falla/$', SearchFalla.as_view(), name='search_falla'),
    url(r'^export/fallas/$', views.export_fallas, name='export_fallas'),
]
