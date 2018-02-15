# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView
)
from django.urls import reverse_lazy
from .forms import (
ActividadForm,
DegradacionForm,
)
from .models import (
Actividad,
Degradacion,
)
import operator
from django.db.models import Q
from functools import reduce
from .resources import ActividadResource, DegradacionResource
from django.http import HttpResponse
from .panels import (
actividades_estado_noc_produccion,
actividades_estado_noc_seguimiento_12h,
actividades_estado_noc_seguimiento_24h,
actividades_estado_noc_seguimiento_36h,
actividades_estado_noc_seguimiento_fo,
actividades_estado_noc_escalado_a_implementacion,
actividades_estado_noc_escalado_a_grupo_calidad,
actividades_estado_noc_escalado_a_rf,
actividades_estado_noc_escalado_a_oym,
actividades_estado_noc_escalado_a_gdrt,
actividades_estado_noc_escalado_control_cambios,
actividades_estado_noc_precheck,
actividades_estado_noc_pendiente_remedy,
actividades_estado_noc_stand_by,
actividades_estado_noc_rollback,
actividades_estado_noc_suspendido,
actividades_estado_noc_none,
)

class ListActividad(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Actividad
    template_name = 'actividad/list_actividad.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListActividad, self).get_queryset()
        qs = self.request.GET.get('qs')
        if qs and qs == 'actividades_estado_noc_produccion':
            queryset = actividades_estado_noc_produccion
        if qs and qs == 'actividades_estado_noc_seguimiento_12h':
            queryset = actividades_estado_noc_seguimiento_12h
        if qs and qs == 'actividades_estado_noc_seguimiento_24h':
            queryset = actividades_estado_noc_seguimiento_24h
        if qs and qs == 'actividades_estado_noc_seguimiento_36h':
            queryset = actividades_estado_noc_seguimiento_36h
        if qs and qs == 'actividades_estado_noc_seguimiento_fo':
            queryset = actividades_estado_noc_seguimiento_fo
        if qs and qs == 'actividades_estado_noc_escalado_a_implementacion':
            queryset = actividades_estado_noc_escalado_a_implementacion
        if qs and qs == 'actividades_estado_noc_escalado_a_grupo_calidad':
            queryset = actividades_estado_noc_escalado_a_grupo_calidad
        if qs and qs == 'actividades_estado_noc_escalado_a_rf':
            queryset = actividades_estado_noc_escalado_a_rf
        if qs and qs == 'actividades_estado_noc_escalado_a_oym':
            queryset = actividades_estado_noc_escalado_a_oym
        if qs and qs == 'actividades_estado_noc_escalado_a_gdrt':
            queryset = actividades_estado_noc_escalado_a_gdrt
        if qs and qs == 'actividades_estado_noc_escalado_control_cambios':
            queryset = actividades_estado_noc_escalado_control_cambios
        if qs and qs == 'actividades_estado_noc_precheck':
            queryset = actividades_estado_noc_precheck
        if qs and qs == 'actividades_estado_noc_pendiente_remedy':
            queryset = actividades_estado_noc_pendiente_remedy
        if qs and qs == 'actividades_estado_noc_stand_by':
            queryset = actividades_estado_noc_stand_by
        if qs and qs == 'actividades_estado_noc_rollback':
            queryset = actividades_estado_noc_rollback
        if qs and qs == 'actividades_estado_noc_suspendido':
            queryset = actividades_estado_noc_suspendido
        if qs and qs == 'actividades_estado_noc_none':
            queryset = actividades_estado_noc_none
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListActividad, self).get_context_data(**kwargs)
        fields = []
        for field in Actividad._meta.fields:
            fields.append(field.name)
        context['actividad_fields'] = fields
        return context

class DetailActividad(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Actividad
    template_name = 'actividad/detail_actividad.html'

class CreateActividad(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ActividadForm
    # template_name = 'actividad/create_actividad.html'
    template_name = 'actividad/includes/partials/create_actividad_modal.html'
    # success_url = reverse_lazy('actividades:list_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super(CreateActividad, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UpdateActividad(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = Actividad
    form_class = ActividadForm
    # concepto_npo_form_class = ConceptoNpoForm
    # template_name = 'actividad/update_actividad.html'
    template_name = 'actividad/includes/partials/update_actividad_modal.html'
    success_url = reverse_lazy('actividades:list_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super(UpdateActividad, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateActividad, self).get_context_data(**kwargs)
    #     context['actividad_form'] = self.get_form()
    #     context['concepto_npo_form'] = self.concepto_npo_form_class()
    #     return context

class DeleteActividad(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = Actividad
    template_name = 'actividad/delete_actividad.html'
    success_url = reverse_lazy('actividades:list_actividad')

class SearchActividad(ListActividad):

    def get_queryset(self):
        result = super(SearchActividad, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(id_notificacion_noc__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(banda__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(valor_wp_eur__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(proyecto__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(escenario__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_trabajo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(grupo_gap__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_noc__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(subestado_noc__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(impacto_degradacion__icontains=q) for q in query_list))
            )
        return result

class FilterActividad(ListActividad):
    paginate_by = 100

    def get_queryset(self):
        queryset = super(FilterActividad, self).get_queryset()
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        query_date = self.request.GET.get('date')
        if query_field and query_value != '':
            if query_field == 'estacion':
                query_dict = { query_field + '__nombre__iexact': query_value }
            else:
                query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        if query_field and query_date != '':
            query_dict = { query_field + '__iexact': query_date }
            queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterActividad, self).get_context_data(**kwargs)
        query_field = self.request.GET.get('field')
        query_value = self.request.GET.get('value')
        query_date = self.request.GET.get('date')
        queryset = Actividad.objects.all()
        if query_field and query_value:
            if query_field == 'estacion':
                query_dict = { query_field + '__nombre__iexact': query_value }
            else:
                query_dict = { query_field + '__iexact': query_value }
            queryset = queryset.filter(**query_dict)
        if query_field and query_date != '':
            query_dict = { query_field + '__iexact': query_date }
            queryset = queryset.filter(**query_dict)
        result = queryset.count()
        context['query_dict'] = query_dict
        context['result'] = result
        return context

def export_actividades(request):
    actividad_resource = ActividadResource()
    query_dict = request.GET.dict()
    queryset = Actividad.objects.filter(**query_dict)
    dataset = actividad_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Actividad.xlsx"'
    return response


class CreateDegradacion(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = DegradacionForm
    # template_name = 'degradacion/create_degradacion.html'
    template_name = 'degradacion/includes/partials/create_degradacion_modal.html'
    # success_url = reverse_lazy('actividades:list_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.perfil= self.request.user.perfil
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateDegradacion, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateDegradacion, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(pk=self.kwargs['pk'])
        return context

class ListDegradacion(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Degradacion
    template_name = 'degradacion/list_degradacion.html'
    paginate_by = 100

class ListDegradacionActividad(ListDegradacion):

    def get_queryset(self, **kwargs):
        queryset = super(ListDegradacion, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class DetailDegradacion(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Degradacion
    template_name = 'degradacion/detail_degradacion.html'

class UpdateDegradacion(LoginRequiredMixin, UpdateView,):
    login_url = 'users:login_user'
    model = Degradacion
    form_class = DegradacionForm
    # template_name = 'degradacion/update_degradacion.html'
    template_name = 'degradacion/includes/partials/update_degradacion_modal.html'
    # success_url = reverse_lazy('actividades:list_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateDegradacion, self).get_context_data(**kwargs)
        context['actividad'] = self.object.actividad
        return context

class DeleteDegradacion(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = Degradacion
    # template_name = 'degradacion/delete_degradacion.html'
    template_name = 'degradacion/includes/partials/delete_degradacion_modal.html'
    # success_url = reverse_lazy('actividades:list_degradacion')

    def get_context_data(self, **kwargs):
        context = super(DeleteDegradacion, self).get_context_data(**kwargs)
        context['actividad'] = self.object.actividad
        return context

    def get_success_url(self):
        actividad = self.object.actividad
        return reverse_lazy( 'actividades:list_degradacion_actividad', kwargs={'pk': actividad.pk})

class SearchDegradacion(ListDegradacion):

    def get_queryset(self):
        queryset = super(SearchDegradacion, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(perfil__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(perfil__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(contenido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_degradaciones(request):
    degradaciones_resource = DegradacionResource()
    dataset = degradaciones_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Degradacion.xlsx"'
    return response
