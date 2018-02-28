# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
Actividad,
Degradacion,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
ActividadResource,
DegradacionResource,
)

# @admin.register(Actividad)
# class ActividadAdmin(admin.ModelAdmin):
#     pass

@admin.register(Actividad)
class ActividadAdmin(ImportExportModelAdmin):
    resource_class = ActividadResource
    list_display = (
    'id',
    'wp',
    'id_notificacion_noc',
    'agrupador',
    'service_supplier',
    'estacion',
    'banda',
    'valor_wp_eur',
    'proyecto',
    'escenario',
    'tipo_trabajo',
    'fecha_ingreso_onair',
    'realtifinish',
    'fecha_integracion',
    'grupo_gap',
    'fecha_estado_noc',
    'estado_noc',
    'subestado_noc',
    'impacto_degradacion',
    'fecha_fc_visita',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = ('creado', 'actualizado')
    search_fields = ['id', 'estacion__nombre']

@admin.register(Degradacion)
class DegradacionAdmin(ImportExportModelAdmin):
    resource_class = DegradacionResource
    list_display = (
    'id',
    'perfil',
    'estacion',
    'actividad',
    'wp',
    'contenido',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
