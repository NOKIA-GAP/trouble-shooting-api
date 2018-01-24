from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
ComentarioNpo,
ComentarioNi,
)
from users.models import Perfil
from estaciones.models import Estacion
from actividades.models import Actividad
from incidentes.models import IncidenteNpo, IncidenteNi

class ComentarioNpoResource(resources.ModelResource):
    npo_ingeniero = fields.Field(
        column_name='npo ingeniero',
        attribute='npo_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    incidente_npo = fields.Field(
        column_name='incidente npo',
        attribute='incidente_npo',
        widget=ForeignKeyWidget(IncidenteNpo, 'pk'))
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'),)
    wp = fields.Field(
        column_name='wp',
        attribute='wp',)
    contenido = fields.Field(
        column_name='contenido',
        attribute='contenido',)
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
        model = ComentarioNpo
        # exclude = ('')
        export_order = (
        'id',
        'npo_ingeniero',
        'incidente_npo',
        'estacion',
        'actividad',
        'wp',
        'contenido',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )

class ComentarioNiResource(resources.ModelResource):
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    incidente_ni = fields.Field(
        column_name='incidente ni',
        attribute='incidente_ni',
        widget=ForeignKeyWidget(IncidenteNi, 'pk'))
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
    contenido = fields.Field(
        column_name='contenido',
        attribute='contenido',)
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
        model = ComentarioNi
        # exclude = ('')
        export_order = (
        'id',
        'ni_ingeniero',
        'incidente_ni',
        'estacion',
        'actividad',
        'wp',
        'contenido',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
