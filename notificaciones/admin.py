from django.contrib import admin

from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
NotificacionFallaSoftware,
NotificacionFallaHardware,
NotificacionFallaDatafill,
NotificacionFallaAjustePotencia,
NotificacionFallaInterferenciaExterna,
NotificacionFallaCambioDiseno,
NotificacionFallaMalRechazo,
NotificacionFallaTX,
NotificacionFallaComportamientoEsperado,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
NotificacionRequiereVisitaResource,
NotificacionFallaInstalacionResource,
NotificacionFallaIntegracionResource,
NotificacionFallaSoftwareResource,
NotificacionFallaHardwareResource,
NotificacionFallaDatafillResource,
NotificacionFallaAjustePotenciaResource,
NotificacionFallaInterferenciaExternaResource,
NotificacionFallaCambioDisenoResource,
NotificacionFallaMalRechazoResource,
NotificacionFallaTXResource,
NotificacionFallaComportamientoEsperadoResource,
)

@admin.register(NotificacionRequiereVisita)
class NotificacionRequiereVisitaAdmin(ImportExportModelAdmin):
    resource_class = NotificacionRequiereVisitaResource
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
    'detalle_solicitud_visita',
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
    'asignacion_ni',
    'actividad',
    'wp',
    'service_supplier',
    'estacion',
    'banda',
    'proyecto',
    'escenario',
    'ni_ingeniero',
    'detalle_falla_instalacion',
    'solver',
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaSoftware)
class NotificacionFallaSoftwareAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaSoftwareResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaHardware)
class NotificacionFallaHardwareAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaHardwareResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaDatafill)
class NotificacionFallaDatafillAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaDatafillResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaAjustePotencia)
class NotificacionFallaAjustePotenciaAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaAjustePotenciaResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']


@admin.register(NotificacionFallaInterferenciaExterna)
class NotificacionFallaInterferenciaExternaAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaInterferenciaExternaResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaCambioDiseno)
class NotificacionFallaCambioDisenoAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaCambioDisenoResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaMalRechazo)
class NotificacionFallaMalRechazoAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaMalRechazoResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaTX)
class NotificacionFallaTXAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaTXResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(NotificacionFallaComportamientoEsperado)
class NotificacionFallaComportamientoEsperadoAdmin(ImportExportModelAdmin):
    resource_class = NotificacionFallaComportamientoEsperadoResource
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
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']
