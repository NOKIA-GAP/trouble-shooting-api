from .models import (
AsignacionNpo,
AsignacionNi,
)
import datetime

# gt mayor que
# gte mayor o igual
# lt menor
# lte menor o igual

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'

TODAY = datetime.date.today()
YESTERDAY = datetime.date.today() - datetime.timedelta(1)
THREEDAYS = datetime.date.today() - datetime.timedelta(3)

# asignaciones npo
asignaciones_npo = AsignacionNpo.objects.all().count()
asignaciones_npo_asignada = AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA).count()
asignaciones_npo_requiere_visita = AsignacionNpo.objects.filter(estado_asignacion=REQUIERE_VISITA).count()
asignaciones_npo_en_monitoreo = AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO).count()
asignaciones_npo_escalado_a_claro = AsignacionNpo.objects.filter(estado_asignacion=ESCALADO_A_CLARO).count()
asignaciones_npo_enviado_a_seguimiento = AsignacionNpo.objects.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO).count()

asignaciones_npo_asignada_previo_hoy = (
    AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY).count()
)
# asignaciones_npo_asignada_previo_hoy_qs = (
#     AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
# )
def asignaciones_npo_asignada_previo_hoy_qs():
    asignaciones_npo_asignada_previo_hoy_qs = AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
    return asignaciones_npo_asignada_previo_hoy_qs

asignaciones_npo_en_monitoreo_tres_dias = (
    AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS).count()
)
# asignaciones_npo_en_monitoreo_tres_dias_qs = (
#     AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO)
# )
def asignaciones_npo_en_monitoreo_tres_dias_qs():
    asignaciones_npo_en_monitoreo_tres_dias_qs = AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS)
    return asignaciones_npo_en_monitoreo_tres_dias_qs.filter(conceptos_npo__creado__lte=THREEDAYS)

# asignaciones ni
asignaciones_ni = AsignacionNi.objects.all().count()
asignaciones_ni_asignada  = AsignacionNi.objects.filter(estado_asignacion=ASIGNADA).count()
asignaciones_ni_requiere_visita = AsignacionNi.objects.filter(estado_asignacion=REQUIERE_VISITA).count()
asignaciones_ni_en_monitoreo = AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO).count()
asignaciones_ni_escalado_a_claro = AsignacionNi.objects.filter(estado_asignacion=ESCALADO_A_CLARO).count()
asignaciones_ni_enviado_a_seguimiento = AsignacionNi.objects.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO).count()

asignaciones_ni_asignada_previo_hoy  = (
    AsignacionNi.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY).count()
)
# asignaciones_ni_asignada_previo_hoy_qs = (
#     AsignacionNi.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
# )
def asignaciones_ni_asignada_previo_hoy_qs():
    asignaciones_ni_asignada_previo_hoy_qs = AsignacionNi.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
    return asignaciones_ni_asignada_previo_hoy_qs

asignaciones_ni_en_monitoreo_tres_dias= (
    AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS).count()
)
# asignaciones_ni_en_monitoreo_tres_dias_qs = (
#     AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO)
# )

def asignaciones_ni_en_monitoreo_tres_dias_qs():
    asignaciones_ni_en_monitoreo_tres_dias_qs = AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS)
    return asignaciones_ni_en_monitoreo_tres_dias_qs.filter(conceptos_ni__creado__lte=THREEDAYS)
