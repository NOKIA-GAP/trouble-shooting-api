# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ReporteActividad
from import_export.admin import ImportExportModelAdmin
from .resources import ReporteActividadResource

@admin.register(ReporteActividad)
class ReporteActividadAdmin(ImportExportModelAdmin):
    resource_class = ReporteActividadResource
