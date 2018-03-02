# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget
from estaciones.models import Estacion
from asignaciones.models import AsignacionNpo, AsignacionNi
from .models import (
Actividad,
Degradacion,
)
from django.utils import timezone
from users.models import Perfil


class ActividadResource(resources.ModelResource):
    wp = fields.Field(
        column_name='wp',
        attribute='wp',
        widget=IntegerWidget())
    id_notificacion_noc = fields.Field(
        column_name='id notificacion noc',
        attribute='id_notificacion_noc',
        widget=IntegerWidget())
    service_supplier = fields.Field(
        column_name='service supplier',
        attribute='service_supplier',)
    field_manager = fields.Field(
        column_name='field manager',
        attribute='field_manager',)
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'nombre'),)
    regional = fields.Field(
        column_name='regional',
        attribute='estacion__regional',)
    ciudad = fields.Field(
        column_name='ciudad',
        attribute='estacion__ciudad',)
    responsable = fields.Field(
        column_name='responsable',
        attribute='estacion__responsable',)
    prioridad = fields.Field(
        column_name='prioridad',
        attribute='estacion__prioridad',)
    valor_wp_eur = fields.Field(
        column_name='valor wp eur',
        attribute='valor_wp_eur',)
    tipo_trabajo = fields.Field(
        column_name='tipo trabajo',
        attribute='tipo_trabajo',)
    fecha_ingreso_onair = fields.Field(
        column_name='fecha ingreso onair',
        attribute='fecha_ingreso_onair',
        widget=DateWidget(format='%d/%m/%Y'))
    realtifinish = fields.Field(
        column_name='realtifinish',
        attribute='realtifinish',
        widget=DateWidget(format='%d/%m/%Y'))
    fecha_integracion = fields.Field(
        column_name='fecha integracion',
        attribute='fecha_integracion',
        widget=DateWidget(format='%d/%m/%Y'))
    grupo_gap = fields.Field(
        column_name='grupo gap',
        attribute='grupo_gap',)
    fecha_estado_noc = fields.Field(
        column_name='fecha estado noc',
        attribute='fecha_estado_noc',
        widget=DateWidget(format='%d/%m/%Y'))
    estado_noc = fields.Field(
        column_name='estado noc',
        attribute='estado_noc',)
    subestado_noc = fields.Field(
        column_name='subestado noc',
        attribute='subestado_noc',)
    impacto_degradacion = fields.Field(
        column_name='impacto degradacion',
        attribute='impacto_degradacion',)
    fecha_fc_visita = fields.Field(
        column_name='fecha fc visita',
        attribute='fecha_fc_visita',
        widget=DateWidget(format='%d/%m/%Y'))

    # asignaciones npo
    npo_ingeniero = fields.Field(
        column_name='npo ingeniero',
        attribute='npo_ingeniero',)
    npo_estado_asignacion = fields.Field(
        column_name='npo estado asignacion',
        attribute='npo_estado_asignacion',)
    npo_concepto = fields.Field(
        column_name='npo concepto',
        attribute='npo_concepto',)
    npo_tipo_intervencion = fields.Field(
        column_name='npo tipo intervencion',
        attribute='npo_tipo_intervencion',)
    npo_fecha_asignacion = fields.Field(
        column_name='npo fecha asignacion',
        attribute='npo_fecha_asignacion',
        widget=DateWidget(format='%d/%m/%Y'))
    npo_fm_supervisor = fields.Field(
        column_name='npo fm supervisor',
        attribute='npo_fm_supervisor',)

    # asignaciones ni
    ni_ingeniero = fields.Field(
        column_name='ni ingeniero',
        attribute='ni_ingeniero',)
    ni_estado_asignacion = fields.Field(
        column_name='ni estado asignacion',
        attribute='ni_estado_asignacion',)
    ni_origen_falla = fields.Field(
        column_name='ni origen falla',
        attribute='ni_origen_falla',)
    ni_solver = fields.Field(
        column_name='ni solver',
        attribute='ni_solver',)
    ni_concepto = fields.Field(
        column_name='ni concepto',
        attribute='ni_concepto',)
    ni_estado_solicitud_hw = fields.Field(
        column_name='ni estado solicitud hw',
        attribute='ni_estado_solicitud_hw',)
    ni_tipo_intervencion = fields.Field(
        column_name='ni tipo intervencion',
        attribute='ni_tipo_intervencion',)
    ni_fecha_asignacion = fields.Field(
        column_name='ni fecha asignacion',
        attribute='ni_fecha_asignacion',
        widget=DateWidget(format='%d/%m/%Y'))
    ni_fm_supervisor = fields.Field(
        column_name='ni fm supervisor',
        attribute='ni_fm_supervisor',)

    # asignaciones npo y asignaciones ni
    estado_ultimo = fields.Field(
        column_name='estado ultimo',
        attribute='estado_ultimo',)
    estado_unico = fields.Field(
        column_name='estado unico',
        attribute='estado_unico',)


    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Actividad
        exclude = ( 'creado', 'actualizado',)
        export_order = (
        # actividad
        'id',
        'wp',
        'id_notificacion_noc',
        'agrupador',
        'service_supplier',
        'field_manager',
        'estacion',
        'regional',
        'ciudad',
        'responsable',
        'prioridad',
        'banda',
        'valor_wp_eur',
        'proyecto',
        'escenario',
        'tipo_trabajo',
        'fecha_ingreso_onair',
        'realtifinish',
        'fecha_integracion',
        'grupo_gap',
        'fecha_estado_noc',
        'estado_noc',
        'subestado_noc',
        'impacto_degradacion',
        'fecha_fc_visita',
        # asignaciones npo
        'npo_ingeniero',
        'npo_estado_asignacion',
        'npo_concepto',
        'npo_tipo_intervencion',
        'npo_fecha_asignacion',
        'npo_fm_supervisor',
        # asignaciones ni
        'ni_ingeniero',
        'ni_estado_asignacion',
        'ni_origen_falla',
        'ni_solver',
        'ni_concepto',
        'ni_estado_solicitud_hw',
        'ni_tipo_intervencion',
        'ni_fecha_asignacion',
        'ni_fm_supervisor',
        # asignaciones npo y asignaciones ni
        'estado_ultimo',
        'estado_unico',
        # actividad
        'estado',
        'subestado',
        )


class DegradacionResource(resources.ModelResource):
    perfil = fields.Field(
        column_name='perfil',
        attribute='perfil',
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
        attribute='wp',
        widget=IntegerWidget())
    contenido = fields.Field(
        column_name='contenido',
        attribute='contenido',)
    creado = fields.Field(
        column_name='creado',
        attribute='creado',
        widget=DateTimeWidget(format='%d/%m/%Y %H:%M:%S'))
    actualizado = fields.Field(
        column_name='actualizado',
        attribute='actualizado',
        widget=DateTimeWidget(format='%d/%m/%Y %H:%M:%S'))

    class Meta:
        model = Degradacion
        exclude = ('imagen')
        export_order = (
        'id',
        'perfil',
        'estacion',
        'actividad',
        'wp',
        'contenido',
        'creado',
        'actualizado',
        )
