from __future__ import unicode_literals

from django.conf.urls import url
from .views import (
# views ComentarioNpo for CRUD
ListComentarioNpo,
DetailComentarioNpo,
UpdateComentarioNpo,
CreateComentarioNpo,
DeleteComentarioNpo,
# views ComentarioNpo for queryset
SearchComentarioNpo,
ListComentarioNpoActividad,
ListComentarioNpoIncidente,
# views ComentarioNi for CRUD
ListComentarioNi,
DetailComentarioNi,
UpdateComentarioNi,
CreateComentarioNi,
DeleteComentarioNi,
# views ComentarioNpo for queryset
SearchComentarioNi,
ListComentarioNiActividad,
ListComentarioNiIncidente,

)
from . import views

app_name = 'comentarios'
urlpatterns = [

    # urls ComentarioNpo for CRUD
    url(r'^list/comentario/npo/$', ListComentarioNpo.as_view(), name='list_comentario_npo'),
    url(r'^create/comentario/npo/(?P<pk>\d+)/$', CreateComentarioNpo.as_view(), name='create_comentario_npo'),
    url(r'^detail/comentario/npo/(?P<pk>\d+)/$', DetailComentarioNpo.as_view(), name='detail_comentario_npo'),
    url(r'^update/comentario/npo/(?P<pk>\d+)/$', UpdateComentarioNpo.as_view(), name='update_comentario_npo'),
    url(r'^delete/comentario/npo/(?P<pk>\d+)/$', DeleteComentarioNpo.as_view(), name='delete_comentario_npo'),

    # urls ComentarioNpo for queryset
    url(r'^search/comentario/npo/$', SearchComentarioNpo.as_view(),
                                            name='search_comentario_npo'),
    url(r'^list/comentario/npo/actividad/(?P<pk>\d+)/$', ListComentarioNpoActividad.as_view(),
                                            name='list_comentario_npo_actividad'),
    url(r'^list/comentario/npo/incidente/(?P<pk>\d+)/$', ListComentarioNpoIncidente.as_view(),
                                            name='list_comentario_npo_incidente'),

    # url ComentarioNpo for export
    url(r'^export/comentarios/npo/$', views.export_comentarios_npo, name='export_comentarios_npo'),

    # urls ComentarioNpo for CRUD
    url(r'^list/comentario/ni/$', ListComentarioNi.as_view(), name='list_comentario_ni'),
    url(r'^create/comentario/ni/(?P<pk>\d+)/$', CreateComentarioNi.as_view(), name='create_comentario_ni'),
    url(r'^detail/comentario/ni/(?P<pk>\d+)/$', DetailComentarioNi.as_view(), name='detail_comentario_ni'),
    url(r'^update/comentario/ni/(?P<pk>\d+)/$', UpdateComentarioNi.as_view(), name='update_comentario_ni'),
    url(r'^delete/comentario/ni/(?P<pk>\d+)/$', DeleteComentarioNi.as_view(), name='delete_comentario_ni'),

    # urls ComentarioNpo for queryset
    url(r'^search/comentario/ni/$', SearchComentarioNi.as_view(),
                                            name='search_comentario_ni'),
    url(r'^list/comentario/ni/actividad/(?P<pk>\d+)/$', ListComentarioNiActividad.as_view(),
                                            name='list_comentario_ni_actividad'),
    url(r'^list/comentario/ni/incidente/(?P<pk>\d+)/$', ListComentarioNiIncidente.as_view(),
                                            name='list_comentario_ni_incidente'),

    # url ComentarioNpo for export
    url(r'^export/comentarios/ni/$', views.export_comentarios_ni, name='export_comentarios_ni'),
]
