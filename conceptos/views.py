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
ConceptoNpoForm,
ConceptoNiForm,
)
from .models import (
ConceptoNpo,
ConceptoNi,
)
import operator
from django.db.models import Q
from functools import reduce
from .resources import ConceptoNpoResource, ConceptoNiResource
from django.http import HttpResponse
from asignaciones.models import AsignacionNpo, AsignacionNi
from actividades.models import Actividad

class CreateConceptoNpo(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ConceptoNpoForm
    # template_name = 'concepto_npo/create_concepto_npo.html'
    template_name = 'concepto_npo/includes/partials/create_concepto_npo_modal.html'
    # success_url = reverse_lazy('actividades:detail_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.npo_ingeniero = self.request.user.perfil
        asignacion = AsignacionNpo.objects.get(pk=self.kwargs['pk'])
        form.instance.asignacion_npo = asignacion
        actividad = asignacion.actividad
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateConceptoNpo, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateConceptoNpo, self).get_context_data(**kwargs)
        context['asignacion_npo'] = AsignacionNpo.objects.get(pk=self.kwargs['pk'])
        return context

class ListConceptoNpo(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = ConceptoNpo
    template_name = 'concepto_npo/list_concepto_npo.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(ListConceptoNpo, self).get_context_data(**kwargs)
        context['conceptos_npo_count'] = self.get_queryset().count()
        return context

class ListConceptoNpoActividad(ListConceptoNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListConceptoNpo, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListConceptoNpoAsignacion(ListConceptoNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListConceptoNpo, self).get_queryset()
        query = AsignacionNpo.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(asignacion_npo_id=query)
        return queryset

class DetailConceptoNpo(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = ConceptoNpo
    template_name = 'concepto_npo/detail_concepto_npo.html'

class UpdateConceptoNpo(LoginRequiredMixin, UpdateView,):
    login_url = 'users:login_user'
    model = ConceptoNpo
    form_class = ConceptoNpoForm
    # template_name = 'concepto_npo/update_concepto_npo.html'
    template_name = 'concepto_npo/includes/partials/update_concepto_npo_modal.html'
    # success_url = reverse_lazy('conceptos:detail_concepto_npo')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateConceptoNpo, self).get_context_data(**kwargs)
        context['asignacion_npo'] = self.object.asignacion_npo
        return context


class DeleteConceptoNpo(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = ConceptoNpo
    # template_name = 'concepto_npo/delete_concepto_npo.html'
    template_name = 'concepto_npo/includes/partials/delete_concepto_npo_modal.html'
    # success_url = reverse_lazy('conceptos:list_concepto_ni_asignacion')

    def get_context_data(self, **kwargs):
        context = super(DeleteConceptoNpo, self).get_context_data(**kwargs)
        context['asignacion_npo'] = self.object.asignacion_npo
        return context

    def get_success_url(self):
        asignacion_npo = self.object.asignacion_npo
        return reverse_lazy( 'conceptos:list_concepto_npo_asignacion', kwargs={'pk': asignacion_npo.pk})

class SearchConceptoNpo(ListConceptoNpo):

    def get_queryset(self):
        queryset = super(SearchConceptoNpo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_ingeniero__apellido__icontains=q) for q in query_list)) |
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

def export_conceptos_npo(request):
    conceptos_npo_resource = ConceptoNpoResource()
    dataset = conceptos_npo_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConceptoNpo.xlsx"'
    return response

class CreateConceptoNi(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ConceptoNiForm
    # template_name = 'concepto_ni/create_concepto_ni.html'
    template_name = 'concepto_ni/includes/partials/create_concepto_ni_modal.html'
    # success_url = reverse_lazy('actividades:detail_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.ni_ingeniero = self.request.user.perfil
        asignacion = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        form.instance.asignacion_ni = asignacion
        actividad = asignacion.actividad
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateConceptoNi, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateConceptoNi, self).get_context_data(**kwargs)
        context['asignacion_ni'] = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        return context



class ListConceptoNi(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = ConceptoNi
    template_name = 'concepto_ni/list_concepto_ni.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(ListConceptoNi, self).get_context_data(**kwargs)
        context['conceptos_ni_count'] = self.get_queryset().count()
        return context

class ListConceptoNiActividad(ListConceptoNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListConceptoNi, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListConceptoNiAsignacion(ListConceptoNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListConceptoNi, self).get_queryset()
        query = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(asignacion_ni_id=query)
        return queryset

class DetailConceptoNi(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = ConceptoNi
    template_name = 'concepto_ni/detail_concepto_ni.html'

class UpdateConceptoNi(LoginRequiredMixin, UpdateView,):
    login_url = 'login_user'
    model = ConceptoNi
    form_class = ConceptoNiForm
    # template_name = 'concepto_ni/update_concepto_ni.html'
    template_name = 'concepto_ni/includes/partials/update_concepto_ni_modal.html'
    # success_url = reverse_lazy('conceptos:detail_concepto_ni')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateConceptoNi, self).get_context_data(**kwargs)
        context['asignacion_ni'] = self.object.asignacion_ni
        return context

class DeleteConceptoNi(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = ConceptoNi
    # template_name = 'concepto_ni/delete_concepto_ni.html'
    template_name = 'concepto_ni/includes/partials/delete_concepto_ni_modal.html'
    # success_url = reverse_lazy('conceptos:list_concepto_ni')

    def get_context_data(self, **kwargs):
        context = super(DeleteConceptoNi, self).get_context_data(**kwargs)
        context['asignacion_ni'] = self.object.asignacion_ni
        return context

    def get_success_url(self):
        asignacion_ni = self.object.asignacion_ni
        return reverse_lazy('conceptos:list_concepto_ni_asignacion', kwargs={'pk': asignacion_ni.pk})


class SearchConceptoNi(ListConceptoNi):

    def get_queryset(self):
        queryset = super(SearchConceptoNi, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
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

def export_conceptos_ni(request):
    conceptos_ni_resource = ConceptoNiResource()
    dataset = conceptos_ni_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ConceptoNi.xlsx"'
    return response
