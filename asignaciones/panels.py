from .models import (
AsignacionNpo,
AsignacionNi,
)
import datetime
from django.utils import timezone
from django.core.cache import cache
from users.models import Perfil

try:
    cache._cache.clear()
except AttributeError:
	old = cache._cull_frequency
	old_max = cache._max_entries
	cache._max_entries = 0
	cache._cull_frequency = 1
	cache._cull()
	cache._cull_frequency = old
	cache._max_entries = old_max

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'

# TODAY = datetime.date.today()
TODAY = timezone.now()
YESTERDAY = timezone.now() - datetime.timedelta(1)
THREEDAYS = timezone.now() - datetime.timedelta(3)

# ingenieros npo
# CESAR_ROJAS = 'Cesar Rojas'
# RAUL_PEREZ = 'Raul Perez'
# JAIRO_POLO = 'Jairo Polo Gonzalez'
# OSCAR_GONZALEZ = 'Oscar Gonzalez'
# JAIME_FIGUEROA = 'Jaime Figueroa'
# WASFI_MABARDI = 'Wasfi Mabardi'
# MAURICIO_RINCON = 'Mauricio Rincon'

# ingenieros ni
# JORGE_ROMERO = 'Jorge Romero'
# JUAN_VALDES = 'Jjuan gabriel valdes'
# YOLAIMA_VERGEL = 'Yolaima Vergel'
# CAROLINA_MANTILLA = 'Carolina Mantilla'
# IVAN_BARRIGA = 'ivan barriga'
# YENIFER_SANCHEZ = 'yenifer sanchez'
# OCTAVIO_TORRADO = 'Octavio Torrado'

# asignaciones npo
asignaciones_npo = AsignacionNpo.objects.all()
asignaciones_npo_asignada = asignaciones_npo.filter(estado_asignacion=ASIGNADA)
asignaciones_npo_requiere_visita = asignaciones_npo.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_npo_en_monitoreo = asignaciones_npo.filter(estado_asignacion=EN_MONITOREO)
asignaciones_npo_escalado_a_claro = asignaciones_npo.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_npo_enviado_a_seguimiento = asignaciones_npo.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_npo_asignada_un_dia = asignaciones_npo.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
asignaciones_npo_en_monitoreo_tres_dias = asignaciones_npo.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_npo__creado__lte=THREEDAYS).distinct()

ingenieros_npo = Perfil.objects.filter(perfil_usuario='NPO Ingeniero')

# asignaciones_npo_ingeniero = asignaciones_npo.filter(estado_asignacion=ASIGNADA, npo_ingeniero=TODAY)

# asignaciones ni
asignaciones_ni = AsignacionNi.objects.all()
asignaciones_ni_asignada = asignaciones_ni.filter(estado_asignacion=ASIGNADA)
asignaciones_ni_requiere_visita = asignaciones_ni.filter(estado_asignacion=REQUIERE_VISITA)
asignaciones_ni_en_monitoreo = asignaciones_ni.filter(estado_asignacion=EN_MONITOREO)
asignaciones_ni_escalado_a_claro = asignaciones_ni.filter(estado_asignacion=ESCALADO_A_CLARO)
asignaciones_ni_enviado_a_seguimiento = asignaciones_ni.filter(estado_asignacion=ENVIADO_A_SEGUIMIENTO)
asignaciones_ni_asignada_un_dia = asignaciones_ni.filter(estado_asignacion=ASIGNADA, fecha_asignacion__lt=TODAY)
asignaciones_ni_en_monitoreo_tres_dias = asignaciones_ni.filter(estado_asignacion=EN_MONITOREO, actualizado__lte=THREEDAYS, conceptos_ni__creado__lte=THREEDAYS).distinct()

ingenieros_ni = Perfil.objects.filter(perfil_usuario='NI Ingeniero')
