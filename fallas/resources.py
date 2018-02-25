# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
Falla,
)
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil

class FallaResource(resources.ModelResource):
    asignacion_ni = fields.Field(
        column_name='asignacion ni',
        attribute='asignacion_ni',
        widget=ForeignKeyWidget(AsignacionNi, 'pk'))
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    wp = fields.Field(
       column_name='wp',
       attribute='wp')
    service_supplier = fields.Field(
       column_name='service supplier',
       attribute='service_supplier')
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'nombre'))
    banda = fields.Field(
       column_name='banda',
       attribute='banda')
    proyecto = fields.Field(
       column_name='proyecto',
       attribute='proyecto')
    escenario = fields.Field(
       column_name='escenario',
       attribute='escenario')
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    concepto = fields.Field(
       column_name='concepto',
       attribute='concepto')
    tipo_falla = fields.Field(
       column_name='tipo falla',
       attribute='tipo_falla')
    creado = fields.Field(
        column_name='creado',
        attribute='creado',
        widget=DateWidget(format='%d/%m/%Y'))
    actualizado = fields.Field(
        column_name='actualizado',
        attribute='actualizado',
        widget=DateWidget(format='%d/%m/%Y'))

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        creado = instance.creado
        if creado:
            instance.creado = creado
            instance.save()

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Falla
        # exclude = (,)
        export_order = (
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
        'tipo_falla',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
