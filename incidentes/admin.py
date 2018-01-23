from django.contrib import admin

from .models import (
IncidenteNpo,
IncidenteNi,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
IncidenteNpoResource,
IncidenteNiResource,
)

@admin.register(IncidenteNpo)
class IncidenteNpoAdmin(ImportExportModelAdmin):
    resource_class = IncidenteNpoResource
    list_display = (
    'id',
    'npo_ingeniero',
    'estacion',
    'actividad',
    'wp',
    'estado_incidente',
    'comentario',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']

@admin.register(IncidenteNi)
class IncidenteNiAdmin(ImportExportModelAdmin):
    resource_class = IncidenteNiResource
    list_display = (
    'id',
    'ni_ingeniero',
    'estacion',
    'actividad',
    'wp',
    'estado_incidente',
    'comentario',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
