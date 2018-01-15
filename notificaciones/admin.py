from django.contrib import admin

from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
NotificacionRequiereVisitaResource,
NotificacionFallaInstalacionResource,
NotificacionFallaIntegracionResource,
)

@admin.register(NotificacionRequiereVisita)
class NotificacionRequiereVisitaAdmin(ImportExportModelAdmin):
    resource_class = NotificacionRequiereVisitaResource
    list_display = (
    'id',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaInstalacion)
class NotificacionFallaInstalacionAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaInstalacionResource
    list_display = (
    'id',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaIntegracion)
class NotificacionFallaIntegracionAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaIntegracionResource
    list_display = (
    'id',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']
