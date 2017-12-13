# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
ConceptoNpo,
ConceptoNi,
)
from import_export.admin import ImportExportModelAdmin
from .resources import (
ConceptoNpoResource,
ConceptoNiResource,
)

@admin.register(ConceptoNpo)
class ConceptoNpoAdmin(ImportExportModelAdmin):
    resource_class = ConceptoNpoResource
    list_display = (
    'id',
    'npo_ingeniero',
    'estacion',
    'actividad',
    'asignacion_npo',
    'wp',
    'contenido',
    'imagen',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']

@admin.register(ConceptoNi)
class ConceptoNiAdmin(ImportExportModelAdmin):
    resource_class = ConceptoNiResource
    list_display = (
    'id',
    'ni_ingeniero',
    'estacion',
    'actividad',
    'asignacion_ni',
    'wp',
    'contenido',
    'imagen',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
