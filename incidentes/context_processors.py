from incidentes.models import IncidenteNpo, IncidenteNi

GAP_ADMINISTRADOR = 'GAP Administrador'
NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'

def incidentes_npo(request):
    incidentes_npo = ''
    if request.user.is_authenticated:
        perfil = request.user.perfil
        if perfil.perfil_usuario == GAP_ADMINISTRADOR:
            incidentes_npo = IncidenteNpo.objects.filter(estado_incidente='Abierto').count()
        if perfil.perfil_usuario == NPO_INGENIERO:
            incidentes_npo = IncidenteNpo.objects.filter(estado_incidente='Abierto', npo_ingeniero=perfil).count()

        return {
            'incidentes_npo': incidentes_npo,
        }
    else:
        return {
            'incidentes_npo': incidentes_npo,
        }

def incidentes_ni(request):
    incidentes_ni = ''
    if request.user.is_authenticated:
        perfil = request.user.perfil
        if perfil.perfil_usuario == GAP_ADMINISTRADOR:
            incidentes_ni = IncidenteNi.objects.filter(estado_incidente='Abierto').count()
        if perfil.perfil_usuario == NI_INGENIERO:
            incidentes_ni = IncidenteNi.objects.filter(estado_incidente='Abierto', ni_ingeniero=perfil).count()

        return {
            'incidentes_ni': incidentes_ni,
        }
    else:
        return {
            'incidentes_ni': incidentes_ni,
        }
