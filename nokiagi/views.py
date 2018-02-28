from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
ListView,
)

from .models import Gi
from actividades.models import Actividad
from estaciones.models import Estacion
from django.utils import timezone
import datetime

THREEDAYS = timezone.now() - datetime.timedelta(3)

PRODUCCION = 'Produccion'
GAP1 = 'GAP1'

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
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True).exclude(onAir__lte=THREEDAYS)
    actividades = Actividad.objects.exclude(estado_noc=PRODUCCION)

    for actividad in actividades:
        try:
            act = actividades_gi.get(wp=actividad.wp)
            if actividad.estado_noc != act.estadoNOC or actividad.subestado_noc != act.subEstadoNOC:
                actividad.estado_noc = act.estadoNOC
                actividad.subestado_noc = act.subEstadoNOC
                actividad.fecha_estado_noc = act.fechaEstado.date()
                actividad.save()
        except Gi.DoesNotExist:
            pass
    return HttpResponse(status=204)

def creacion(request):
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True).exclude(estadoNOC__exact=PRODUCCION)
    actividades = Actividad.objects.all()

    for actividad_gi in actividades_gi:
        try:
            act = actividades.get(wp=actividad_gi.wp)
        except Actividad.DoesNotExist:
            try:
                est = Estacion.objects.get(nombre=actividad_gi.siteName)
                Actividad.objects.create(
                    wp=actividad_gi.wp,
                    agrupador=actividad_gi.agrupadores,
                    service_supplier=actividad_gi.ss,
                    estacion=est,
                    banda=actividad_gi.banda,
                    proyecto=actividad_gi.proyecto,
                    escenario=actividad_gi.escenario,
                    realtifinish=actividad_gi.realTiFinish,
                    fecha_integracion=actividad_gi.fechaIntegracion,
                    fecha_estado_noc=actividad_gi.fechaEstado,
                    estado_noc=actividad_gi.estadoNOC,
                    subestado_noc=actividad_gi.subEstadoNOC,
                )
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    nombre=actividad_gi.siteName,
                    regional=actividad_gi.region,
                    ciudad=actividad_gi.ciudad,
                    responsable=GAP1,
                )
                Actividad.objects.create(
                    wp=actividad_gi.wp,
                    agrupador=actividad_gi.agrupadores,
                    service_supplier=actividad_gi.ss,
                    estacion=estacion,
                    banda=actividad_gi.banda,
                    proyecto=actividad_gi.proyecto,
                    escenario=actividad_gi.escenario,
                    realtifinish=actividad_gi.realTiFinish,
                    fecha_integracion=actividad_gi.fechaIntegracion,
                    fecha_estado_noc=actividad_gi.fechaEstado,
                    estado_noc=actividad_gi.estadoNOC,
                    subestado_noc=actividad_gi.subEstadoNOC,
                )
    return HttpResponse(status=204)
