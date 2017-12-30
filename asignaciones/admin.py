# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
AsignacionNpo,
AsignacionNi,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
AsignacionNpoResource,
AsignacionNiResource,
)

# Register your models here.
@admin.register(AsignacionNpo)
class AsignacionNpoAdmin(ImportExportModelAdmin):
    resource_class = AsignacionNpoResource
    list_display = (
    'id',
    'npo_asignador',
    'npo_ingeniero',
    'npo_ingeniero_celular',
    'npo_ingeniero_empresa',
    'fm_supervisor',
    'fm_supervisor_celular',
    'fm_supervisor_empresa',
    'estacion',
    'actividad',
    'wp',
    'estado_asignacion',
    'tipo_intervencion',
    'fecha_asignacion',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']

@admin.register(AsignacionNi)
class AsignacionNiAdmin(ImportExportModelAdmin):
    resource_class = AsignacionNiResource
    list_display = (
    'id',
    'ni_asignador',
    'ni_ingeniero',
    'ni_ingeniero_celular',
    'ni_ingeniero_empresa',
    'fm_supervisor',
    'fm_supervisor_celular',
    'fm_supervisor_empresa',
    'estacion',
    'actividad',
    'wp',
    'estado_asignacion',
    'origen_falla',
    'tipo_intervencion',
    'fecha_asignacion',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
