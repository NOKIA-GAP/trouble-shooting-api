from django.contrib import admin

from .models import (
Falla,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
FallaResource,
)

@admin.register(Falla)
class FallaAdmin(ImportExportModelAdmin):
    resource_class = FallaResource
    list_display = (
    'id',
    'asignacion_ni',
    'actividad',
    'wp',
    'service_supplier',
    'estacion',
    'banda',
    'proyecto',
    'escenario',
    'ni_ingeniero',
    'concepto',
    'tipo_falla',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']
