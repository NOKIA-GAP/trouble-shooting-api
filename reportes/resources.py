# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import DateWidget
from .models import (
ReporteActividad,
)

class ReporteActividadResource(resources.ModelResource):
    valor_wp_eur = fields.Field(
        column_name='valor wp eur',
        attribute='valor_wp_eur',)
    fecha_integracion = fields.Field(
        column_name='fecha integracion',
        attribute='fecha_integracion',
        widget=DateWidget(format='%d/%m/%Y'))
    grupo_gap = fields.Field(
        column_name='grupo gap',
        attribute='grupo_gap',)
    tipo_trabajo_noc = fields.Field(
        column_name='tipo trabajo noc',
        attribute='tipo_trabajo_noc',)
    estado_noc = fields.Field(
        column_name='estado noc',
        attribute='estado_noc',)
    subestado_noc = fields.Field(
        column_name='subestado noc',
        attribute='subestado_noc',)
    responsable_ni = fields.Field(
        column_name='responsable ni',
        attribute='responsable_ni',)
    estado_ni = fields.Field(
        column_name='estado ni',
        attribute='estado_ni',)
    concepto_ni = fields.Field(
        column_name='concepto ni',
        attribute='concepto_ni',)
    tipo_intervencion_ni = fields.Field(
        column_name='tipo intervencion ni',
        attribute='tipo_intervencion_ni',)
    fecha_asignacion_ni = fields.Field(
        column_name='fecha asignacion ni',
        attribute='fecha_asignacion_ni',
        widget=DateWidget(format='%d/%m/%Y'))
    requiere_hw = fields.Field(
        column_name='requiere hw',
        attribute='requiere_hw',)
    responsable_actual = fields.Field(
        column_name='responsable actual',
        attribute='reresponsable_actual',)
    responsable_npo = fields.Field(
        column_name='responsable npo',
        attribute='responsable_npo',)
    estado_npo = fields.Field(
        column_name='estado npo',
        attribute='estado_npo',)
    posible_causa = fields.Field(
        column_name='posible causa',
        attribute='posible_causa',)
    concepto_npo = fields.Field(
        column_name='concepto npo',
        attribute='concepto_npo',)
    tipo_intervencion_npo = fields.Field(
        column_name='tipo intervencion npo',
        attribute='tipo_intervencion_npo',)
    fecha_asignacion_npo = fields.Field(
        column_name='fecha asignacion npo',
        attribute='fecha_asignacion_npo',
        widget=DateWidget(format='%d/%m/%Y'))
    fecha_fc_visita = fields.Field(
        column_name='fecha fc visita',
        attribute='fecha_fc_visita',
        widget=DateWidget(format='%d/%m/%Y'))
    id_siteaccess = fields.Field(
        column_name='id siteaccess',
        attribute='id_siteaccess',)

    class Meta:
        model = ReporteActividad
        exclude = (
        'id',
        'gap_administrador',
        'creado',
        'actualizado'
        )
        export_order = (
        'wp',
        'agrupador',
        'estacion',
        'regional',
        'ciudad',
        'banda',
        'valor_wp_eur',
        'proyecto',
        'escenario',
        'fecha_integracion',
        'grupo_gap',
        'tipo_trabajo_noc',
        'estado_noc',
        'subestado_noc',
        'responsable_ni',
        'estado_ni',
        'concepto_ni',
        'tipo_intervencion_ni',
        'fecha_asignacion_ni',
        'requiere_hw',
        'responsable_actual',
        'responsable_npo',
        'estado_npo',
        'posible_causa',
        'concepto_npo',
        'tipo_intervencion_npo',
        'fecha_asignacion_npo',
        'supervisor',
        'fecha_fc_visita',
        'id_siteaccess',
        )
