# -*- coding: utf-8 -*-
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
NotificacionFallaSoftware,
NotificacionFallaHardware,
NotificacionFallaDatafill,
NotificacionFallaAjustePotencia,
NotificacionFallaInterferenciaExterna,
NotificacionFallaCambioDiseno,
NotificacionFallaMalRechazo,
NotificacionFallaTX,
NotificacionFallaComportamientoEsperado,
NotificacionFallaComportamientoPrevio,
)
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil

class NotificacionRequiereVisitaResource(resources.ModelResource):
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
    detalle_solicitud_visita = fields.Field(
       column_name='detalle solicitud visita',
       attribute='detalle_solicitud_visita')
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
        model = NotificacionRequiereVisita
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
        'detalle_solicitud_visita',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaInstalacionResource(resources.ModelResource):
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
    detalle_falla_instalacion= fields.Field(
       column_name='detalle falla instalacion',
       attribute='detalle_falla_instalacion')
    solver = fields.Field(
       column_name='solver',
       attribute='solver')
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
        model = NotificacionFallaInstalacion
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
        'detalle_falla_instalacion',
        'solver',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaIntegracionResource(resources.ModelResource):
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
        model = NotificacionFallaIntegracion
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaSoftwareResource(resources.ModelResource):
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
        model = NotificacionFallaSoftware
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaHardwareResource(resources.ModelResource):
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
        model = NotificacionFallaHardware
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaDatafillResource(resources.ModelResource):
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
        model = NotificacionFallaDatafill
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaAjustePotenciaResource(resources.ModelResource):
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
        model = NotificacionFallaAjustePotencia
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaInterferenciaExternaResource(resources.ModelResource):
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
        model = NotificacionFallaInterferenciaExterna
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaCambioDisenoResource(resources.ModelResource):
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
        model = NotificacionFallaCambioDiseno
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaMalRechazoResource(resources.ModelResource):
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
        model = NotificacionFallaMalRechazo
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaTXResource(resources.ModelResource):
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
        model = NotificacionFallaTX
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaComportamientoEsperadoResource(resources.ModelResource):
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
        model = NotificacionFallaComportamientoEsperado
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )

class NotificacionFallaComportamientoPrevioResource(resources.ModelResource):
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
        model = NotificacionFallaComportamientoPrevio
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
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
