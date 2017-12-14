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
from .forms import SolicitudHWForm, SolicitudForm, SolicitudHWUpdateForm, SolicitudFormSet
from .models import SolicitudHW, Solicitud
import operator
from django.db.models import Q
from functools import reduce
from .resources import SolicitudHWResource
from django.http import HttpResponse
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from django.db import transaction

class CreateSolicitudHW(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = SolicitudHWForm
    # solicitud_form_class = SolicitudForm
    template_name = 'solicitudhw/includes/partials/create_solicitudhw_modal.html'

    # def form_valid(self, form):
    #     form.instance.ni_ingeniero = self.request.user.perfil
    #     asignacion = AsignacionNi.objects.get(pk=self.kwargs['pk'])
    #     form.instance.asignacion_ni = asignacion
    #     actividad = asignacion.actividad
    #     form.instance.estacion = actividad.estacion
    #     form.instance.actividad = actividad
    #     form.instance.wp = actividad.wp
    #     return super(CreateSolicitudHW, self).form_valid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CreateSolicitudHW, self).get_context_data(**kwargs)
    #     context['solicitudhw_form'] = self.get_form()
    #     context['solicitud_form'] = self.solicitud_form_class()
    #     context['asignacion_ni'] = AsignacionNi.objects.get(pk=self.kwargs['pk'])
    #     return context

    def get_context_data(self, **kwargs):
        context = super(CreateSolicitudHW, self).get_context_data(**kwargs)
        if self.request.POST:
            context['solicitudes'] = SolicitudFormSet(self.request.POST)
            context['asignacion_ni'] = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        else:
            context['solicitudes'] = SolicitudFormSet()
            context['asignacion_ni'] = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super(CreateSolicitudHW, self).get_form_kwargs()
        asignacion_ni = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        kwargs.update({'asignacion_ni': asignacion_ni})
        return kwargs

    def form_valid(self, form):
        form.instance.ni_ingeniero = self.request.user.perfil
        asignacion = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        form.instance.asignacion_ni = asignacion
        actividad = asignacion.actividad
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp

        context = self.get_context_data()
        solicitudes = context['solicitudes']
        with transaction.atomic():
            self.object = form.save()

            if solicitudes.is_valid():
                solicitudes.instance = self.object
                solicitudes.save()
        return super(CreateSolicitudHW, self).form_valid(form)

class DetailSolicitudHW(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = SolicitudHW
    template_name = 'solicitudhw/detail_solicitudhw.html'

class ListSolicitudHW(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = SolicitudHW
    template_name = 'solicitudhw/list_solicitudhw.html'
    paginate_by = 100

class ListSolicitudHWActividad(ListSolicitudHW):

    def get_queryset(self, **kwargs):
        queryset = super(ListSolicitudHW, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListSolicitudHWAsignacion(ListSolicitudHW):

    def get_queryset(self, **kwargs):
        queryset = super(ListSolicitudHW, self).get_queryset()
        query = AsignacionNi.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(asignacion_ni_id=query)
        return queryset

class UpdateSolicitudHW(LoginRequiredMixin, UpdateView,):
    login_url = 'login_user'
    model = SolicitudHW
    form_class = SolicitudHWUpdateForm
    template_name = 'solicitudhw/includes/partials/update_solicitudhw_modal.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateSolicitudHW, self).get_context_data(**kwargs)
        context['asignacion_ni'] = self.object.asignacion_ni
        return context

class DeleteSolicitudHW(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = SolicitudHW
    template_name = 'solicitudhw/includes/partials/delete_solicitudhw_modal.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteSolicitudHW, self).get_context_data(**kwargs)
        context['asignacion_ni'] = self.object.asignacion_ni
        return context

    def get_success_url(self):
        asignacion_ni = self.object.asignacion_ni
        return reverse_lazy( 'solicitudeshw:list_solicitudhw_asignacion', kwargs={'pk': asignacion_ni.pk})

class SearchSolicitudHW(ListSolicitudHW):

    def get_queryset(self):
        queryset = super(SearchSolicitudHW, self).get_queryset()
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
                          (Q(estado_solicitud__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

def export_solicitudeshw(request):
    solicitudeshw_resource = SolicitudHWResource()
    dataset = solicitudeshw_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="SolicitudHW.xlsx"'
    return response

class ListSolicitud(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = Solicitud
    template_name = 'solicitud/list_solicitud.html'
    paginate_by = 100

class ListSolicitudSolicitudHW(ListSolicitud):

    def get_queryset(self, **kwargs):
        queryset = super(ListSolicitud, self).get_queryset()
        query = SolicitudHW.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(solicitudhw_id=query)
        return queryset

class DetailSolicitud(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Solicitud
    template_name = 'solicitud/detail_solicitud.html'

class UpdateSolicitud(LoginRequiredMixin, UpdateView,):
    login_url = 'login_user'
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'solicitud/includes/partials/update_solicitud_modal.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateSolicitud, self).get_context_data(**kwargs)
        context['solicitudhw'] = self.object.solicitudhw
        return context

class DeleteSolicitud(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = Solicitud
    template_name = 'solicitud/includes/partials/delete_solicitud_modal.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteSolicitud, self).get_context_data(**kwargs)
        context['solicitudhw'] = self.object.solicitudhw
        return context

    def get_success_url(self):
        solicitudhw = self.object.solicitudhw
        return reverse_lazy( 'solicitudeshw:list_solicitud_solicitudhw', kwargs={'pk': solicitudhw.pk})
