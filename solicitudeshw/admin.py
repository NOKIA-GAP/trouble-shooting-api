# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SolicitudHW, Solicitud
from import_export.admin import ImportExportModelAdmin
from .resources import SolicitudHWResource

# @admin.register(SolicitudHW)
# class SolicitudHWAdmin(admin.ModelAdmin):
#     pass

@admin.register(SolicitudHW)
class SolicitudHWAdmin(ImportExportModelAdmin):
    resource_class = SolicitudHWResource
    list_display = (
    'id',
    'ni_ingeniero',
    'asignacion_ni',
    'estacion',
    'actividad',
    'wp',
    'estado_solicitud',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'solicitudhw',
    'hardware',
    'cantidad',
    'descripcion',
    'creado',
    'actualizado',
    'estado',
    'subestado',
    )
    search_fields = ['id']
