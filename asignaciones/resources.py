# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
AsignacionNpo,
AsignacionNi,
)
from users.models import Perfil
from estaciones.models import Estacion
from actividades.models import Actividad
from conceptos.models import ConceptoNi, ConceptoNpo

class AsignacionNpoResource(resources.ModelResource):
    npo_asignador = fields.Field(
        column_name='npo asignador',
        attribute='npo_asignador',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    npo_ingeniero = fields.Field(
        column_name='npo ingeniero',
        attribute='npo_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    npo_ingeniero_celular = fields.Field(
        column_name='npo ingeniero celular',
        attribute='npo_ingeniero_celular',)
    npo_ingeniero_empresa = fields.Field(
        column_name='npo ingeniero empresa',
        attribute='npo_ingeniero_empresa',)
    fm_supervisor = fields.Field(
        column_name='fm supervisor',
        attribute='fm_supervisor',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'))
    fm_supervisor_celular = fields.Field(
        column_name='fm supervisor celular',
        attribute='fm_supervisor_celular',)
    fm_supervisor_empresa = fields.Field(
        column_name='fm supervisor empresa',
        attribute='fm_supervisor_empresa',)
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    banda = fields.Field(
       column_name='banda',
       attribute='actividad__banda',)
    proyecto = fields.Field(
       column_name='proyecto',
       attribute='actividad__proyecto',)
    escenario = fields.Field(
       column_name='escenario',
       attribute='actividad__escenario',)
    tipo_trabajo = fields.Field(
       column_name='tipo trabajo',
       attribute='actividad__tipo_trabajo',)
    estado_asignacion = fields.Field(
        column_name='estado asignacion',
        attribute='estado_asignacion',)
    npo_concepto = fields.Field(
        column_name='npo concepto',
        attribute='npo_concepto',)
    tipo_intervencion = fields.Field(
        column_name='tipo intervencion',
        attribute='tipo_intervencion',)
    fecha_asignacion = fields.Field(
        column_name='fecha asignacion',
        attribute='fecha_asignacion',
        widget=DateWidget(format='%d/%m/%Y'))
    creado = fields.Field(
        column_name='creado',
        attribute='creado',
        widget=DateWidget(format='%d/%m/%Y'))
    actualizado = fields.Field(
        column_name='actualizado',
        attribute='actualizado',
        widget=DateWidget(format='%d/%m/%Y'))

    # def save_instance(self, instance, using_transactions=True, dry_run=False):
        # variables
        # logics
        # instance.atribute = something
        # instance.save()

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = AsignacionNpo
        # exclude = ('npo_concepto',)
        export_order = (
        'id',
        'npo_asignador',
        'npo_ingeniero',
        'npo_ingeniero_celular',
        'npo_ingeniero_empresa',
        'fm_supervisor',
        'fm_supervisor_celular',
        'fm_supervisor_empresa',
        'estacion',
        'actividad',
        'wp',
        'banda',
        'proyecto',
        'escenario',
        'tipo_trabajo',
        'estado_asignacion',
        'npo_concepto',
        'tipo_intervencion',
        'fecha_asignacion',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class AsignacionNiResource(resources.ModelResource):
    ni_asignador = fields.Field(
        column_name='ni asignador',
        attribute='ni_asignador',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'),)
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'),)
    ni_ingeniero_celular = fields.Field(
        column_name='ni ingeniero celular',
        attribute='ni_ingeniero_celular',)
    ni_ingeniero_empresa = fields.Field(
        column_name='ni ingeniero empresa',
        attribute='ni_ingeniero_empresa',)
    fm_supervisor = fields.Field(
        column_name='fm supervisor',
        attribute='fm_supervisor',
        widget=ForeignKeyWidget(Perfil, 'nombre_completo'),)
    fm_supervisor_celular = fields.Field(
        column_name='fm supervisor celular',
        attribute='fm_supervisor_celular',)
    fm_supervisor_empresa = fields.Field(
        column_name='fm supervisor empresa',
        attribute='fm_supervisor_empresa',)
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion__nombre',)
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'),)
    banda = fields.Field(
       column_name='banda',
       attribute='actividad__banda',)
    proyecto = fields.Field(
       column_name='proyecto',
       attribute='actividad__proyecto',)
    escenario = fields.Field(
       column_name='escenario',
       attribute='actividad__escenario',)
    tipo_trabajo = fields.Field(
       column_name='tipo trabajo',
       attribute='actividad__tipo_trabajo',)
    estado_asignacion = fields.Field(
        column_name='estado asignacion',
        attribute='estado_asignacion',)
    origen_falla = fields.Field(
        column_name='origen falla',
        attribute='origen_falla',)
    solver = fields.Field(
        column_name='solver',
        attribute='solver',)
    ni_concepto = fields.Field(
        column_name='ni concepto',
        attribute='ni_concepto',)
    tipo_intervencion = fields.Field(
        column_name='tipo intervencion',
        attribute='tipo_intervencion',)
    fecha_asignacion = fields.Field(
        column_name='fecha asignacion',
        attribute='fecha_asignacion',
        widget=DateWidget(format='%d/%m/%Y'))
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
        model = AsignacionNi
        # exclude = ('ni_concepto',)
        export_order = (
        'id',
        'ni_asignador',
        'ni_ingeniero',
        'ni_ingeniero_celular',
        'ni_ingeniero_empresa',
        'fm_supervisor',
        'fm_supervisor_celular',
        'fm_supervisor_empresa',
        'estacion',
        'actividad',
        'wp',
        'banda',
        'proyecto',
        'escenario',
        'tipo_trabajo',
        'estado_asignacion',
        'origen_falla',
        'solver',
        'ni_concepto',
        'tipo_intervencion',
        'fecha_asignacion',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
