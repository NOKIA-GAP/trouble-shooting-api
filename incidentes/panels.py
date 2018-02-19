from .models import IncidenteNpo, IncidenteNi

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

# incidentes npo
incidentes_npo = IncidenteNpo.objects.all()
incidentes_npo_abierto = incidentes_npo.filter(estado_incidente=ABIERTO)
incidentes_npo_cerrado = incidentes_npo.filter(estado_incidente=CERRADO)

# incidentes ni
incidentes_ni = IncidenteNi.objects.all()
incidentes_ni_abierto = incidentes_ni.filter(estado_incidente=ABIERTO)
incidentes_ni_cerrado = incidentes_ni.filter(estado_incidente=CERRADO)
