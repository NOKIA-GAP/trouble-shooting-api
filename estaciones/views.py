# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  CreateView,
                                  DeleteView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import EstacionForm
from .models import Estacion
import operator
from django.db.models import Q
from functools import reduce
from .resources import EstacionResource
from django.http import HttpResponse
from .panels import (
estaciones_estado_produccion,
estaciones_estado_enviado_a_seguimiento,
estaciones_estado_escalado_a_claro,
estaciones_estado_en_monitoreo,
estaciones_estado_requiere_visita,
estaciones_estado_asignada,
estaciones_estado_none,
)

class ListEstacion(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Estacion
    template_name = 'estacion/list_estacion.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListEstacion, self).get_queryset()
        qs = self.request.GET.get('qs')
        if qs and qs == 'estaciones_estado_produccion':
            queryset = estaciones_estado_produccion
        if qs and qs == 'estaciones_estado_enviado_a_seguimiento':
            queryset = estaciones_estado_enviado_a_seguimiento
        if qs and qs == 'estaciones_estado_escalado_a_claro':
            queryset = estaciones_estado_escalado_a_claro
        if qs and qs == 'estaciones_estado_en_monitoreo':
            queryset = estaciones_estado_en_monitoreo
        if qs and qs == 'estaciones_estado_requiere_visita':
            queryset = estaciones_estado_requiere_visita
        if qs and qs == 'estaciones_estado_asignada':
            queryset = estaciones_estado_asignada
        if qs and qs == 'estaciones_estado_none':
            queryset = estaciones_estado_none
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListEstacion, self).get_context_data(**kwargs)
        fields = []
        for field in Estacion._meta.fields:
            fields.append(field.name)
        context['estaciones_count'] = Estacion.objects.all().count()
        context['estacion_fields'] = fields
        return context

class DetailEstacion(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Estacion
    template_name = 'estacion/detail_estacion.html'

class CreateEstacion(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = EstacionForm
    # template_name = 'estacion/create_estacion.html'
    template_name = 'estacion/includes/partials/create_estacion_modal.html'
    # success_url = reverse_lazy('estaciones:list_estacion')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

class UpdateEstacion(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = Estacion
    form_class = EstacionForm
    # template_name = 'estacion/update_estacion.html'
    template_name = 'estacion/includes/partials/update_estacion_modal.html'
    # success_url = reverse_lazy('estaciones:detail_estacion')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

class DeleteEstacion(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = Estacion
    template_name = 'estacion/delete_estacion.html'
    success_url = reverse_lazy('estaciones:list_estacion')

class SearchEstacion(ListEstacion):

    def get_queryset(self):
        queryset = super(SearchEstacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(regional__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ciudad__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(responsable__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(prioridad__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchEstacion, self).get_context_data(**kwargs)
        result = self.object_list.count()
        context['result'] = result
        return context

class FilterEstacion(ListEstacion):
    paginate_by = 100

    def get_queryset(self):
        queryset = super(FilterEstacion, self).get_queryset()
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        if query_field and query_value:
            query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterEstacion, self).get_context_data(**kwargs)
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        queryset = Estacion.objects.all()
        if query_field and query_value:
            query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        result = queryset.count()
        context['result'] = result
        return context

def export_estaciones(request):
    estacion_resource = EstacionResource()
    dataset = estacion_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Estacion.xlsx"'
    return response
