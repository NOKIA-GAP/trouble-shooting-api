from .models import Estacion

PRODUCCION = 'Produccion'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
ESCALADO_A_CLARO = 'Escalado a claro'
EN_MONITOREO = 'En monitoreo'
REQUIERE_VISITA = 'Requiere visita'
ASIGNADA = 'Asignada'

estaciones = Estacion.objects.all()
estaciones_estado_produccion = estaciones.filter(estado_estacion=PRODUCCION)
estaciones_estado_enviado_a_seguimiento = estaciones.filter(estado_estacion=ENVIADO_A_SEGUIMIENTO)
estaciones_estado_escalado_a_claro = estaciones.filter(estado_estacion=ESCALADO_A_CLARO)
estaciones_estado_en_monitoreo = estaciones.filter(estado_estacion=EN_MONITOREO)
estaciones_estado_requiere_visita = estaciones.filter(estado_estacion=REQUIERE_VISITA)
estaciones_estado_asignada = estaciones.filter(estado_estacion=ASIGNADA)
estaciones_estado_none = estaciones.filter(estado_estacion=None)
