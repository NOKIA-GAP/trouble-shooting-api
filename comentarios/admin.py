from django.contrib import admin
from .models import (
ComentarioNpo,
ComentarioNi,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
ComentarioNpoResource,
ComentarioNiResource,
)

@admin.register(ComentarioNpo)
class ComentarioNpoAdmin(ImportExportModelAdmin):
    resource_class = ComentarioNpoResource
    list_display = (
    'id',
    'npo_ingeniero',
    'incidente_npo',
    'estacion',
    'actividad',
    'wp',
    'contenido',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']

@admin.register(ComentarioNi)
class ComentarioNiAdmin(ImportExportModelAdmin):
    resource_class = ComentarioNiResource
    list_display = (
    'id',
    'ni_ingeniero',
    'incidente_ni',
    'estacion',
    'actividad',
    'wp',
    'contenido',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
