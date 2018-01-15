# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
)
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil

class NotificacionRequiereVisitaResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = NotificacionRequiereVisita
        # exclude = (,)
        export_order = (
        'id',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaInstalacionResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = NotificacionFallaInstalacion
        # exclude = (,)
        export_order = (
        'id',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaIntegracionResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = NotificacionFallaIntegracion
        # exclude = (,)
        export_order = (
        'id',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
