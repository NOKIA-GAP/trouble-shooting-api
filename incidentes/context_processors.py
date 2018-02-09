from incidentes.models import IncidenteNpo, IncidenteNi

GAP_ADMINISTRADOR = 'GAP Administrador'
NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'

def notificacion_incidentes_npo(request):
    notificacion_incidentes_npo = ''
    if request.user.is_authenticated:
        perfil = request.user.perfil
        if perfil.perfil_usuario == GAP_ADMINISTRADOR:
            notificacion_incidentes_npo = IncidenteNpo.objects.filter(estado_incidente='Abierto').count()
        if perfil.perfil_usuario == NPO_INGENIERO:
            notificacion_incidentes_npo = IncidenteNpo.objects.filter(estado_incidente='Abierto', npo_ingeniero=perfil).count()

        return {
            'notificacion_incidentes_npo': notificacion_incidentes_npo,
        }
    else:
        return {
            'notificacion_incidentes_npo': notificacion_incidentes_npo,
        }

def notificacion_incidentes_ni(request):
    notificacion_incidentes_ni = ''
    if request.user.is_authenticated:
        perfil = request.user.perfil
        if perfil.perfil_usuario == GAP_ADMINISTRADOR:
            notificacion_incidentes_ni = IncidenteNi.objects.filter(estado_incidente='Abierto').count()
        if perfil.perfil_usuario == NI_INGENIERO:
            notificacion_incidentes_ni = IncidenteNi.objects.filter(estado_incidente='Abierto', ni_ingeniero=perfil).count()

        return {
            'notificacion_incidentes_ni': notificacion_incidentes_ni,
        }
    else:
        return {
            'notificacion_incidentes_ni': notificacion_incidentes_ni,
        }
