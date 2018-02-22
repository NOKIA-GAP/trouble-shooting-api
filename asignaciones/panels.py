from .models import (
AsignacionNpo,
AsignacionNi,
)
import datetime
from django.utils import timezone
from users.models import Perfil

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'

# TODAY = datetime.date.today()
# TODAY = timezone.now()
YESTERDAY = timezone.now() - datetime.timedelta(1)
THREEDAYS = timezone.now() - datetime.timedelta(3)

NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'

# asignaciones npo
asignaciones_npo = AsignacionNpo.objects.all()
asignaciones_npo_asignada = asignaciones_npo.filter(estado_asignacion=ASIGNADA)
asignaciones_npo_requiere_visita = asignaciones_npo.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_npo_en_monitoreo = asignaciones_npo.filter(estado_asignacion=EN_MONITOREO)
asignaciones_npo_escalado_a_claro = asignaciones_npo.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_npo_enviado_a_seguimiento = asignaciones_npo.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_npo_asignada_un_dia = asignaciones_npo.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=timezone.now())
asignaciones_npo_en_monitoreo_tres_dias = asignaciones_npo.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_npo__creado__lte=THREEDAYS).distinct()

ingenieros_npo = Perfil.objects.filter(perfil_usuario=NPO_INGENIERO)

# asignaciones ni
asignaciones_ni = AsignacionNi.objects.all()
asignaciones_ni_asignada = asignaciones_ni.filter(estado_asignacion=ASIGNADA)
asignaciones_ni_requiere_visita = asignaciones_ni.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_ni_en_monitoreo = asignaciones_ni.filter(estado_asignacion=EN_MONITOREO)
asignaciones_ni_escalado_a_claro = asignaciones_ni.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_ni_enviado_a_seguimiento = asignaciones_ni.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_ni_asignada_un_dia = asignaciones_ni.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=timezone.now())
asignaciones_ni_en_monitoreo_tres_dias = asignaciones_ni.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_ni__creado__lte=THREEDAYS).distinct()

ingenieros_ni = Perfil.objects.filter(perfil_usuario=NI_INGENIERO)
