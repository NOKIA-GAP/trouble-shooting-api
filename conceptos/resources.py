# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
ConceptoNpo,
ConceptoNi,
)
from users.models import Perfil
from estaciones.models import Estacion
from actividades.models import Actividad
from asignaciones.models import AsignacionNpo, AsignacionNi

class ConceptoNpoResource(resources.ModelResource):
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
        widget=ForeignKeyWidget(Actividad, 'pk'),)
    asignacion_npo = fields.Field(
        column_name='asignacion npo',
        attribute='asignacion_npo',
        widget=ForeignKeyWidget(AsignacionNpo, 'pk'))
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
        model = ConceptoNpo
        exclude = ('imagen')
        export_order = (
        'id',
        'npo_ingeniero',
        'estacion',
        'actividad',
        'asignacion_npo',
        'wp',
        'contenido',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )

class ConceptoNiResource(resources.ModelResource):
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
    asignacion_ni = fields.Field(
        column_name='asignacion ni',
        attribute='asignacion_ni',
        widget=ForeignKeyWidget(AsignacionNi, 'pk'))
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
        model = ConceptoNi
        exclude = ('imagen')
        export_order = (
        'id',
        'ni_ingeniero',
        'estacion',
        'actividad',
        'asignacion_ni',
        'wp',
        'contenido',
        'estado',
        'subestado',
        'creado',
        'actualizado',
        )
