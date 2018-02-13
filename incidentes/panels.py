from .models import IncidenteNpo, IncidenteNi

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

# incidentes npo
incidentes_npo = IncidenteNpo.objects.all()
incidentes_npo_abierto = IncidenteNpo.objects.filter(estado_incidente=ABIERTO)
incidentes_npo_cerrado = IncidenteNpo.objects.filter(estado_incidente=CERRADO)

# incidentes ni
incidentes_ni = IncidenteNi.objects.all()
incidentes_ni_abierto = IncidenteNi.objects.filter(estado_incidente=ABIERTO)
incidentes_ni_cerrado = IncidenteNi.objects.filter(estado_incidente=CERRADO)
