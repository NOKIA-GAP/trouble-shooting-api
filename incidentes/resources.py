from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
IncidenteNpo,
IncidenteNi,
)
from users.models import Perfil
from estaciones.models import Estacion
from actividades.models import Actividad

class IncidenteNpoResource(resources.ModelResource):
    npo_ingeniero = fields.Field(
        column_name='npo ingeniero',
        attribute='npo_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    wp = fields.Field(
        column_name='wp',
        attribute='wp',)
    estado_incidente = fields.Field(
        column_name='estado incidente',
        attribute='estado_incidente',)
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
        model = IncidenteNpo
        # exclude = ('',)
        export_order = (
        'id',
        'npo_ingeniero',
        'estacion',
        'actividad',
        'wp',
        'estado_incidente',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class IncidenteNiResource(resources.ModelResource):
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    wp = fields.Field(
        column_name='wp',
        attribute='wp',)
    estado_incidente = fields.Field(
        column_name='estado incidente',
        attribute='estado_incidente',)
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
        model = IncidenteNpo
        # exclude = ('',)
        export_order = (
        'id',
        'ni_ingeniero',
        'estacion',
        'actividad',
        'wp',
        'estado_incidente',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
