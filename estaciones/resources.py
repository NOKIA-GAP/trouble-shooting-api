# -*- coding: utf-8 -*-s
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Estacion

class EstacionResource(resources.ModelResource):
    estado_estacion = fields.Field(
        column_name='estado estacion',
        attribute='estado_estacion',)
    numero_actividades = fields.Field(
        column_name='numero actividades',
        attribute='numero_actividades',)
    creado = fields.Field(
        column_name='creado',
        attribute='creado',
        widget=DateWidget(format='%d/%m/%Y'))
    actualizado = fields.Field(
        column_name='actualizado',
        attribute='actualizado',
        widget=DateWidget(format='%d/%m/%Y'))

    class Meta:
        model = Estacion
        # exclude = ( '', )
        export_order = (
        'id',
        'nombre',
        'regional',
        'ciudad',
        'responsable',
        'prioridad',
        'estado_estacion',
        'numero_actividades',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
