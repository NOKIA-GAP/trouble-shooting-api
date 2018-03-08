from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import (
Alerta
)
from estaciones.models import Estacion
from actividades.models import Actividad

class AlertaResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'nombre'))
    actividad = fields.Field(
        column_name='actividad',
        attribute='actividad',
        widget=ForeignKeyWidget(Actividad, 'pk'))
    wp = fields.Field(
        column_name='wp',
        attribute='wp',)
    mensaje = fields.Field(
        column_name='mensaje',
        attribute='mensaje',)
    estado_alerta = fields.Field(
        column_name='estado alerta',
        attribute='estado_alerta',)
    tipo_alerta = fields.Field(
        column_name='tipo alerta',
        attribute='tipo_alerta',)
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
        model = Alerta
        # exclude = ('',)
        export_order = (
        'id',
        'estacion',
        'actividad',
        'wp',
        'mensaje',
        'estado_alerta',
        'tipo_alerta',
        'creado',
        'actualizado',
        'estado',
        'subestado',
        )
