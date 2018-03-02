from django.shortcuts import render
from django.http import HttpResponse
from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
NotificacionFallaMalRechazo,
)
from .resources import (
NotificacionRequiereVisitaResource,
NotificacionFallaInstalacionResource,
NotificacionFallaIntegracionResource,
NotificacionFallaMalRechazoResource,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

import operator
from django.db.models import Q
from functools import reduce

class ListNotificacionRequiereVisita(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionRequiereVisita
    template_name = 'notificacion_requiere_visita/list_notificacion_requiere_visita.html'
    paginate_by = 100

class SearchNotificacionRequiereVisita(ListNotificacionRequiereVisita):

    def get_queryset(self):
        queryset = super(SearchNotificacionRequiereVisita, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(asignacion_ni__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(service_supplier__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_notificaciones_requiere_visita(request):
    notificaciones_requiere_visita = NotificacionRequiereVisitaResource()
    dataset = notificaciones_requiere_visita.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionRequiereVisita.xlsx"'
    return response

class ListNotificacionFallaInstalacion(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaInstalacion
    template_name = 'notificacion_falla_instalacion/list_notificacion_falla_instalacion.html'
    paginate_by = 100

class SearchNotificacionFallaInstalacion(ListNotificacionFallaInstalacion):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaInstalacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(asignacion_ni__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(service_supplier__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(solver__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_notificaciones_falla_instalacion(request):
    notificaciones_falla_instalacion = NotificacionFallaInstalacionResource()
    dataset = notificaciones_falla_instalacion.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaInstalacion.xlsx"'
    return response

class ListNotificacionFallaIntegracion(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaIntegracion
    template_name = 'notificacion_falla_integracion/list_notificacion_falla_integracion.html'
    paginate_by = 100

class SearchNotificacionFallaIntegracion(ListNotificacionFallaIntegracion):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaIntegracion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(asignacion_ni__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(service_supplier__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_notificaciones_falla_integracion(request):
    notificaciones_falla_integracion = NotificacionFallaIntegracionResource()
    dataset = notificaciones_falla_integracion.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaIntegracion.xlsx"'
    return response

class ListNotificacionFallaMalRechazo(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaMalRechazo
    template_name = 'notificacion_falla_mal_rechazo/list_notificacion_falla_mal_rechazo.html'
    paginate_by = 100

class SearchNotificacionFallaMalRechazo(ListNotificacionFallaMalRechazo):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaMalRechazo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(asignacion_ni__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(service_supplier__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_notificaciones_falla_mal_rechazo(request):
    notificaciones_falla_mal_rechazo = NotificacionFallaMalRechazoResource()
    dataset = notificaciones_falla_mal_rechazo.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaMalRechazo.xlsx"'
    return response
