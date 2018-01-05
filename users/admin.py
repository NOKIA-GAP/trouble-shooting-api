# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Perfil
from import_export.admin import ImportExportModelAdmin
from .resources import PerfilResource

# @admin.register(Perfil)
# class PerfilAdmin(admin.ModelAdmin):
#    pass

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
    resource_class = PerfilResource
    list_display = (
    'id',
    'user',
    'slug',
    'perfil_usuario',
    'nombre',
    'apellido',
    'nombre_completo',
    'email',
    'celular',
    'creado',
    'actualizado',
    )
    search_fields = ['nombre_completo']
