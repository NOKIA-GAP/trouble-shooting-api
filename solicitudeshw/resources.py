# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, IntegerWidget
from .models import SolicitudHW
from users.models import Perfil
from asignaciones.models import AsignacionNi
from estaciones.models import Estacion
from actividades.models import Actividad

class SolicitudHWResource(resources.ModelResource):
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    asignacion_ni = fields.Field(
        column_name='asignacion ni',
        attribute='asignacion_ni',
        widget=ForeignKeyWidget(AsignacionNi, 'pk'))
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    wp = fields.Field(
        column_name='wp',
        attribute='wp',
        widget=IntegerWidget())
    estado_solicitud = fields.Field(
        column_name='estado solicitud',
        attribute='estado_solicitud',)
    creado = fields.Field(
        column_name='creado',
        attribute='creado',
        widget=DateWidget(format='%d/%m/%Y'))
    actualizado = fields.Field(
        column_name='actualizado',
        attribute='actualizado',
        widget=DateWidget(format='%d/%m/%Y'))


    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = SolicitudHW
        # exclude = ('',)
        export_order = (
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
