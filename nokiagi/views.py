from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
ListView,
)

from .models import Gi
from actividades.models import Actividad
from estaciones.models import Estacion
from alertas.models import Alerta
from django.utils import timezone
import datetime
import operator
from django.db.models import Q
from functools import reduce

THREEDAYS = timezone.now() - datetime.timedelta(3)

PRODUCCION = 'Produccion'
GAP1 = 'GAP1'
ABIERTO = 'Abierto'
NORMALIZACION = 'Normalizacion'

class ListGi(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Gi
    template_name = 'gi/list_gi.html'
    paginate_by = 100

    def get_queryset(self):
        queryset = super(ListGi, self).get_queryset()
        queryset = Gi.objects.exclude(fechaIntegracion__isnull=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListGi, self).get_context_data(**kwargs)
        fields = []
        for field in Gi._meta.fields:
            fields.append(field.name)
        context['gi_fields'] = fields
        context['gi_count'] = Gi.objects.exclude(fechaIntegracion__isnull=True).count()
        return context

        return context

class SearchGi(ListGi):

    def get_queryset(self):
        queryset = super(SearchGi, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
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
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchGi, self).get_context_data(**kwargs)
        result = self.object_list.count()
        context['result'] = result
        return context

class FilterGi(ListGi):
    paginate_by = 100

    def get_queryset(self):
        queryset = super(FilterGi, self).get_queryset()
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        query_date = self.request.GET.get('date')
        if query_field and query_value != '':
            query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        if query_field and query_date != '':
            query_dict = { query_field + '__iexact': query_date }
            queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterGi, self).get_context_data(**kwargs)
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        query_date = self.request.GET.get('date')
        queryset = Gi.objects.exclude(fechaIntegracion__isnull=True)
        if query_field and query_value:
            query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        if query_field and query_date != '':
            query_dict = { query_field + '__iexact': query_date }
            queryset = queryset.filter(**query_dict)
        result = queryset.count()
        context['query_dict'] = query_dict
        context['result'] = result
        return context

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
                estacion = Estacion.objects.get(nombre=actividad_gi.siteName)
                actividad = Actividad.objects.create(
                    wp=actividad_gi.wp,
                    agrupador=actividad_gi.agrupadores,
                    service_supplier=actividad_gi.ss,
                    field_manager=actividad_gi.fm,
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
            except Estacion.DoesNotExist:
                estacion = Estacion.objects.create(
                    nombre=actividad_gi.siteName,
                    regional=actividad_gi.region,
                    ciudad=actividad_gi.ciudad,
                    responsable=GAP1,
                )
                actividad = Actividad.objects.create(
                    wp=actividad_gi.wp,
                    agrupador=actividad_gi.agrupadores,
                    service_supplier=actividad_gi.ss,
                    field_manager=actividad_gi.fm,
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

def normalizacion(request):
    # if request.headers["X-Appengine-Cron"]:
    actividades_gi = Gi.objects.exclude(fechaIntegracion__isnull=True)
    actividades = Actividad.objects.all()
    for actividad_gi in actividades_gi:
        try:
            actividad = actividades.get(wp=actividad_gi.wp)
            if not actividad.fecha_integracion:
                mensaje = 'La actividad no tiene fecha de integración.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if not actividad.estado_noc:
                mensaje = 'La actividad no tiene estado noc.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if actividad.estado_noc and actividad.estado_noc != actividad_gi.estadoNOC:
                mensaje = 'La actividad tiene estado noc diferente.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if not actividad.banda:
                mensaje = 'La actividad no tiene banda.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if actividad.banda and actividad.banda != actividad_gi.banda:
                mensaje = 'La actividad tiene banda diferente.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if not actividad.proyecto:
                mensaje = 'La actividad no tiene proyecto.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if actividad.proyecto and actividad.proyecto != actividad_gi.proyecto:
                mensaje = 'La actividad tiene proyecto diferente.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if not actividad.escenario:
                mensaje = 'La actividad no tiene escenario.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
            if actividad.escenario and actividad.escenario != actividad_gi.escenario:
                mensaje = 'La actividad tiene escenario diferente.'
                alerta = Alerta.objects.create(
                    estacion=actividad.estacion,
                    actividad=actividad,
                    wp=actividad.wp,
                    mensaje=mensaje,
                    estado_alerta=ABIERTO,
                    tipo_alerta=NORMALIZACION,
                )
        except Actividad.DoesNotExist:
            pass
    return HttpResponse(status=204)
