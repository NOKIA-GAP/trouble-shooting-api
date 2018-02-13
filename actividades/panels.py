from .models import (
Actividad,
Degradacion
)

PRODUCCION = 'Produccion'
SEGUIMIENTO_12H ='Seguimiento 12h'
SEGUIMIENTO_24H = 'Seguimiento 24h'
SEGUIMIENTO_36H = 'Seguimiento 36h'
SEGUIMIENTO_FO = 'Seguimiento FO'
ESCALADO_A_IMPLEMENTACION = 'Escalado a Implementacion'
ESCALADO_A_GRUPO_CALIDAD = 'Escalado a Grupo Calidad'
ESCALADO_A_RF = 'Escalado a RF'
ESCALADO_A_OYM = 'Escalado a OyM'
ESCALADO_A_GDRT = 'Escalado a GDRT'
ESCALADO_CONTROL_CAMBIOS = 'Escalado Control Cambios'
PRECHECK = 'PreCheck'
PENDIENTE_REMEDY = 'Pendiente Remedy'
STAND_BY = 'Stand By'
ROLLBACK = 'Rollback'
SUSPENDIDO = 'Suspendido'

actividades = Actividad.objects.all()
actividades_estado_noc_produccion = Actividad.objects.filter(estado_noc=PRODUCCION)
actividades_estado_noc_seguimiento_12h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_12H)
actividades_estado_noc_seguimiento_24h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_24H)
actividades_estado_noc_seguimiento_36h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_36H)
actividades_estado_noc_seguimiento_fo = Actividad.objects.filter(estado_noc=SEGUIMIENTO_FO)
actividades_estado_noc_escalado_a_implementacion = Actividad.objects.filter(estado_noc=ESCALADO_A_IMPLEMENTACION)
actividades_estado_noc_escalado_a_grupo_calidad = Actividad.objects.filter(estado_noc=ESCALADO_A_GRUPO_CALIDAD)
actividades_estado_noc_escalado_a_rf = Actividad.objects.filter(estado_noc=ESCALADO_A_RF)
actividades_estado_noc_escalado_a_oym = Actividad.objects.filter(estado_noc=ESCALADO_A_OYM)
actividades_estado_noc_escalado_a_gdrt = Actividad.objects.filter(estado_noc=ESCALADO_A_GDRT)
actividades_estado_noc_escalado_control_cambios = Actividad.objects.filter(estado_noc=ESCALADO_CONTROL_CAMBIOS)
actividades_estado_noc_precheck = Actividad.objects.filter(estado_noc=PRECHECK)
actividades_estado_noc_pendiente_remedy = Actividad.objects.filter(estado_noc=PENDIENTE_REMEDY)
actividades_estado_noc_stand_by = Actividad.objects.filter(estado_noc=STAND_BY)
actividades_estado_noc_rollback = Actividad.objects.filter(estado_noc=ROLLBACK)
actividades_estado_noc_suspendido = Actividad.objects.filter(estado_noc=SUSPENDIDO)
