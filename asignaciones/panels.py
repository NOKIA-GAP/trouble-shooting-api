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

asignaciones_npo = AsignacionNpo.objects.none()
asignaciones_ni = AsignacionNi.objects.none()

# asignaciones npo
asignaciones_npo = AsignacionNpo.objects.all()
asignaciones_npo_asignada = AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA)
asignaciones_npo_requiere_visita = AsignacionNpo.objects.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_npo_en_monitoreo = AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO)
asignaciones_npo_escalado_a_claro = AsignacionNpo.objects.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_npo_enviado_a_seguimiento = AsignacionNpo.objects.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_npo_asignada_un_dia = AsignacionNpo.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=timezone.now())
asignaciones_npo_en_monitoreo_tres_dias = AsignacionNpo.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_npo__creado__lte=THREEDAYS).distinct()

ingenieros_npo = Perfil.objects.filter(perfil_usuario=NPO_INGENIERO)

# asignaciones ni
asignaciones_ni = AsignacionNi.objects.all()
asignaciones_ni_asignada = AsignacionNi.objects.filter(estado_asignacion=ASIGNADA)
asignaciones_ni_requiere_visita = AsignacionNi.objects.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_ni_en_monitoreo = AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO)
asignaciones_ni_escalado_a_claro = AsignacionNi.objects.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_ni_enviado_a_seguimiento = AsignacionNi.objects.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_ni_asignada_un_dia = AsignacionNi.objects.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=timezone.now())
asignaciones_ni_en_monitoreo_tres_dias = AsignacionNi.objects.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_ni__creado__lte=THREEDAYS).distinct()

ingenieros_ni = Perfil.objects.filter(perfil_usuario=NI_INGENIERO)
