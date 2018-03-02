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
import operator
from django.db.models import Q
from functools import reduce

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

class SearchGi(ListGi):

    def get_queryset(self):
        result = super(SearchGi, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(agrupadores__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(siteName__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(region__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ciudad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ss__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fm__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(onAir__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(realTiFinish__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fechaIntegracion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(fechaEstado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estadoNOC__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(subEstadoNOC__icontains=q) for q in query_list))
            )
        return result

# def actualizacion(request):
#     actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True).exclude(onAir__lte=THREEDAYS)
#     actividades = Actividad.objects.exclude(estado_noc=PRODUCCION)
#
#     for actividad in actividades:
#         try:
#             act = actividades_gi.get(wp=actividad.wp)
#             if actividad.estado_noc != act.estadoNOC or actividad.subestado_noc != act.subEstadoNOC:
#                 actividad.estado_noc = act.estadoNOC
#                 actividad.subestado_noc = act.subEstadoNOC
#                 actividad.fecha_estado_noc = act.fechaEstado.date()
#                 actividad.save()
#         except Gi.DoesNotExist:
#             pass
#     return HttpResponse(status=204)

def actualizacion(request):
    # if request.headers["X-Appengine-Cron"]:
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True).exclude(onAir__lte=THREEDAYS)
    actividades = Actividad.objects.exclude(estado_noc=PRODUCCION)

    for actividad_gi in actividades_gi:
        try:
            actividad = actividades.get(wp=actividad_gi.wp)
            if actividad.estado_noc != actividad_gi.estadoNOC or actividad.subestado_noc != actividad_gi.subEstadoNOC:
                actividad.estado_noc = actividad_gi.estadoNOC
                actividad.subestado_noc = actividad_gi.subEstadoNOC
                actividad.fecha_estado_noc = actividad_gi.fechaEstado.date()
                actividad.save()
        except Actividad.DoesNotExist:
            pass
    return HttpResponse(status=204)

def creacion(request):
    # if request.headers["X-Appengine-Cron"]:
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True).exclude(estadoNOC__exact=PRODUCCION)
    actividades = Actividad.objects.all()

    for actividad_gi in actividades_gi:
        try:
            actividad = actividades.get(wp=actividad_gi.wp)
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