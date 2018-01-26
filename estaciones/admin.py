# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Estacion
from import_export.admin import ImportExportModelAdmin
from .resources import EstacionResource

#@admin.register(Estacion)
#class EstacionAdmin(admin.ModelAdmin):
#    pass

@admin.register(Estacion)
class EstacionAdmin(ImportExportModelAdmin):
    resource_class = EstacionResource
    list_display = (
    'id',
    'nombre',
    'regional',
    'ciudad',
    'responsable',
    'prioridad',
    'estado_estacion',
    'numero_actividades',
    )
    search_fields = ['id', 'nombre']
