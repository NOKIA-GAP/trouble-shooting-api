from django.shortcuts import render
from django.http import HttpResponse
from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
NotificacionFallaSoftware,
NotificacionFallaHardware,
NotificacionFallaDatafill,
NotificacionFallaAjustePotencia,
NotificacionFallaInterferenciaExterna,
NotificacionFallaCambioDiseno,
NotificacionFallaMalRechazo,
NotificacionFallaTX,
NotificacionFallaComportamientoEsperado,
NotificacionFallaComportamientoPrevio,
)
from .resources import (
NotificacionRequiereVisitaResource,
NotificacionFallaInstalacionResource,
NotificacionFallaIntegracionResource,
NotificacionFallaSoftwareResource,
NotificacionFallaHardwareResource,
NotificacionFallaDatafillResource,
NotificacionFallaAjustePotenciaResource,
NotificacionFallaInterferenciaExternaResource,
NotificacionFallaCambioDisenoResource,
NotificacionFallaMalRechazoResource,
NotificacionFallaTXResource,
NotificacionFallaComportamientoEsperadoResource,
NotificacionFallaComportamientoPrevioResource,
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

class ListNotificacionFallaSoftware(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaSoftware
    template_name = 'notificacion_falla_software/list_notificacion_falla_software.html'
    paginate_by = 100

class SearchNotificacionFallaSoftware(ListNotificacionFallaSoftware):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaSoftware, self).get_queryset()
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

def export_notificaciones_falla_software(request):
    notificaciones_falla_software = NotificacionFallaSoftwareResource()
    dataset = notificaciones_falla_software.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaSoftware.xlsx"'
    return response

class ListNotificacionFallaHardware(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaHardware
    template_name = 'notificacion_falla_hardware/list_notificacion_falla_hardware.html'
    paginate_by = 100

class SearchNotificacionFallaHardware(ListNotificacionFallaHardware):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaHardware, self).get_queryset()
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

def export_notificaciones_falla_hardware(request):
    notificaciones_falla_hardware = NotificacionFallaHardwareResource()
    dataset = notificaciones_falla_hardware.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaHardware.xlsx"'
    return response

class ListNotificacionFallaDatafill(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaDatafill
    template_name = 'notificacion_falla_datafill/list_notificacion_falla_datafill.html'
    paginate_by = 100

class SearchNotificacionFallaDatafill(ListNotificacionFallaDatafill):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaDatafill, self).get_queryset()
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

def export_notificaciones_falla_datafill(request):
    notificaciones_falla_datafill = NotificacionFallaDatafillResource()
    dataset = notificaciones_falla_datafill.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaDatafill.xlsx"'
    return response

class ListNotificacionFallaAjustePotencia(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaAjustePotencia
    template_name = 'notificacion_falla_ajuste_potencia/list_notificacion_falla_ajuste_potencia.html'
    paginate_by = 100

class SearchNotificacionFallaAjustePotencia(ListNotificacionFallaAjustePotencia):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaAjustePotencia, self).get_queryset()
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

def export_notificaciones_falla_ajuste_potencia(request):
    notificaciones_falla_ajuste_potencia = NotificacionFallaAjustePotenciaResource()
    dataset = notificaciones_falla_ajuste_potencia.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaAjustePotencia.xlsx"'
    return response

class ListNotificacionFallaInterferenciaExterna(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaInterferenciaExterna
    template_name = 'notificacion_falla_interferencia_externa/list_notificacion_falla_interferencia_externa.html'
    paginate_by = 100

class SearchNotificacionFallaInterferenciaExterna(ListNotificacionFallaInterferenciaExterna):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaInterferenciaExterna, self).get_queryset()
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

def export_notificaciones_falla_interferencia_externa(request):
    notificaciones_falla_interferencia_externa = NotificacionFallaInterferenciaExternaResource()
    dataset = notificaciones_falla_interferencia_externa.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaInterferenciaExterna.xlsx"'
    return response

class ListNotificacionFallaCambioDiseno(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaCambioDiseno
    template_name = 'notificacion_falla_cambio_diseno/list_notificacion_falla_cambio_diseno.html'
    paginate_by = 100

class SearchNotificacionFallaCambioDiseno(ListNotificacionFallaCambioDiseno):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaCambioDiseno, self).get_queryset()
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

def export_notificaciones_falla_cambio_diseno(request):
    notificaciones_falla_cambio_diseno = NotificacionFallaCambioDisenoResource()
    dataset = notificaciones_falla_cambio_diseno.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaCambioDiseno.xlsx"'
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

class ListNotificacionFallaTX(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaTX
    template_name = 'notificacion_falla_tx/list_notificacion_falla_tx.html'
    paginate_by = 100

class SearchNotificacionFallaTX(ListNotificacionFallaTX):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaTX, self).get_queryset()
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

def export_notificaciones_falla_tx(request):
    notificaciones_falla_tx = NotificacionFallaTXResource()
    dataset = notificaciones_falla_tx.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaTX.xlsx"'
    return response

class ListNotificacionFallaComportamientoEsperado(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaComportamientoEsperado
    template_name = 'notificacion_falla_comportamiento_esperado/list_notificacion_falla_comportamiento_esperado.html'
    paginate_by = 100

class SearchNotificacionFallaComportamientoEsperado(ListNotificacionFallaComportamientoEsperado):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaComportamientoEsperado, self).get_queryset()
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

def export_notificaciones_falla_comportamiento_esperado(request):
    notificaciones_falla_comportamiento_esperado = NotificacionFallaComportamientoEsperadoResource()
    dataset = notificaciones_falla_comportamiento_esperado.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaComportamientoEsperado.xlsx"'
    return response

class ListNotificacionFallaComportamientoPrevio(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = NotificacionFallaComportamientoPrevio
    template_name = 'notificacion_falla_comportamiento_previo/list_notificacion_falla_comportamiento_previo.html'
    paginate_by = 100

class SearchNotificacionFallaComportamientoPrevio(ListNotificacionFallaComportamientoPrevio):

    def get_queryset(self):
        queryset = super(SearchNotificacionFallaComportamientoPrevio, self).get_queryset()
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

def export_notificaciones_falla_comportamiento_previo(request):
    notificaciones_falla_comportamiento_previo = NotificacionFallaComportamientoPrevioResource()
    dataset = notificaciones_falla_comportamiento_previo.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaComportamientoPrevio.xlsx"'
    return response
