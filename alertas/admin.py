from django.contrib import admin

from .models import (
Alerta
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
AlertaResource
)

@admin.register(Alerta)
class AlertaAdmin(ImportExportModelAdmin):
    resource_class = AlertaResource
    list_display = (
    'id',
    'estacion',
    'actividad',
    'wp',
    'mensaje',
    'estado_alerta',
    'tipo_alerta',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
