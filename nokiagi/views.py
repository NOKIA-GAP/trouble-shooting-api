from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
ListView,
)

from .models import Gi
from actividades.models import Actividad
from estaciones.models import Estacion

PRODUCCION = 'Produccion'

class ListGi(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Gi
    template_name = 'gi/list_gi.html'
    paginate_by = 100

    def get_queryset(self):
        queryset = super(ListGi, self).get_queryset()
        queryset = Gi.objects.exclude(fechaIntegracion__isnull=True)
        return queryset

def actualizacion(request):
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True)
    actividades = Actividad.objects.exclude(estado_noc=PRODUCCION)

    for actividad in actividades:
        try:
            act = actividades_gi.get(wp=actividad.wp)
            if act:
                print (act)
                if actividad.estado_noc != act.estadoNOC:
                    actividad.estado_noc = act.estadoNOC
                    actividad.subestado_noc = act.subEstadoNOC
                    actividad.fecha_estado_noc = act.fechaEstado
                    print (actividad.estado_noc, actividad.subestado_noc, actividad.fecha_estado_noc )
                    # actividad.save()
        except Gi.DoesNotExist:
            pass
    return request
