from django.shortcuts import render
from django.http import HttpResponse
from .models import (
Falla
)
from .resources import (
FallaResource
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

import operator
from django.db.models import Q
from functools import reduce

INSTALACION = 'Instalacion'
SOFTWARE = 'Software'
HARDWARE = 'Hardware'
DATAFILL = 'Datafill'
AJUSTEPOTENCIA = 'Ajuste Potencia'
INTEGRACION = 'Integracion'
INTERFERENCIAEXTREMA = 'Interferencia externa'
CAMBIODISENO = 'Cambio diseno'
MALRECHAZO = 'Mal rechazo'
TX = 'TX'
COMPORTAMIENTOESPERADO = 'Comportamiento esperado'
COMPORTAMIENTOPREVIO = 'Comportamiento previo'
AJUSTEADYACENCIAS = 'Ajuste Adyacencias'

class ListFalla(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Falla
    template_name = 'falla/list_falla.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        print(self.request.path)
        queryset = super(ListFalla, self).get_queryset()
        qs = self.request.GET.get('qs')
        if qs == INSTALACION:
            print(self.request)
            queryset = Falla.objects.filter(tipo_falla=INSTALACION)
        if qs == SOFTWARE:
            queryset = Falla.objects.filter(tipo_falla=SOFTWARE)
        if qs == HARDWARE:
            queryset = Falla.objects.filter(tipo_falla=HARDWARE)
        if qs == DATAFILL:
            queryset = Falla.objects.filter(tipo_falla=DATAFILL)
        if qs == AJUSTEPOTENCIA:
            queryset = Falla.objects.filter(tipo_falla=AJUSTEPOTENCIA)
        if qs == INTEGRACION:
            queryset = Falla.objects.filter(tipo_falla=INTEGRACION)
        if qs == INTERFERENCIAEXTREMA:
            queryset = Falla.objects.filter(tipo_falla=INTERFERENCIAEXTREMA)
        if qs == CAMBIODISENO:
            queryset = Falla.objects.filter(tipo_falla=CAMBIODISENO)
        if qs == MALRECHAZO:
            queryset = Falla.objects.filter(tipo_falla=MALRECHAZO)
        if qs == TX:
            queryset = Falla.objects.filter(tipo_falla=TX)
        if qs == COMPORTAMIENTOPREVIO:
            queryset = Falla.objects.filter(tipo_falla=COMPORTAMIENTOPREVIO)
        if qs == AJUSTEADYACENCIAS:
            queryset = Falla.objects.filter(tipo_falla=AJUSTEADYACENCIAS)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListFalla, self).get_context_data(**kwargs)
        context['fallas_count'] = self.get_queryset().count()
        return context

class SearchFalla(ListFalla):

    def get_queryset(self):
        queryset = super(SearchFalla, self).get_queryset()
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
                          (Q(tipo_falla__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_fallas(request):
    fallas = FallaResource()
    queryset = Falla.objects.all()
    qs = request.GET.get('qs')
    if qs == INSTALACION:
        queryset = Falla.objects.filter(tipo_falla=INSTALACION)
    if qs == SOFTWARE:
        queryset = Falla.objects.filter(tipo_falla=SOFTWARE)
    if qs == HARDWARE:
        queryset = Falla.objects.filter(tipo_falla=HARDWARE)
    if qs == DATAFILL:
        queryset = Falla.objects.filter(tipo_falla=DATAFILL)
    if qs == AJUSTEPOTENCIA:
        queryset = Falla.objects.filter(tipo_falla=AJUSTEPOTENCIA)
    if qs == INTEGRACION:
        queryset = Falla.objects.filter(tipo_falla=INTEGRACION)
    if qs == INTERFERENCIAEXTREMA:
        queryset = Falla.objects.filter(tipo_falla=INTERFERENCIAEXTREMA)
    if qs == CAMBIODISENO:
        queryset = Falla.objects.filter(tipo_falla=CAMBIODISENO)
    if qs == MALRECHAZO:
        queryset = Falla.objects.filter(tipo_falla=MALRECHAZO)
    if qs == TX:
        queryset = Falla.objects.filter(tipo_falla=TX)
    if qs == COMPORTAMIENTOPREVIO:
        queryset = Falla.objects.filter(tipo_falla=COMPORTAMIENTOPREVIO)
    if qs == AJUSTEADYACENCIAS:
        queryset = Falla.objects.filter(tipo_falla=AJUSTEADYACENCIAS)

    dataset = fallas.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Falla.xlsx"'
    return response
