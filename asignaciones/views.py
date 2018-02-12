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
AsignacionNpoForm,
AsignacionNiForm,
AsignacionNpoIngenieroForm,
AsignacionNpoAsiganadorForm,
AsignacionNiAsignadorForm,
AsignacionNiIngenieroForm,
)
from .models import (
AsignacionNpo,
AsignacionNi,
)
import operator
from django.db.models import Q
from functools import reduce
from .resources import AsignacionNpoResource, AsignacionNiResource
from django.http import HttpResponse
from actividades.models import Actividad
from users.models import Perfil
import datetime
from . import choices
from .panels import (
asignaciones_npo_asignada_previo_hoy_qs,
asignaciones_ni_asignada_previo_hoy_qs,
asignaciones_npo_en_monitoreo_tres_dias_qs,
asignaciones_ni_en_monitoreo_tres_dias_qs,
)

ASIGNADA = 'Asignada'
EN_MONITOREO = 'En monitoreo'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
REQUIERE_VISITA = 'Requiere visita'
NO_EXITOSA = 'No exitosa'
ESCALADO_A_CLARO = 'Escalado a claro'

NI_ASIGNADOR = 'NI Asignador'
NPO_ASIGNADOR = 'NPO Asignador'
NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'
FM_LIDER = 'FM Lider'
GAP_ADMINISTRADOR = 'GAP Administrador'

class CreateAsignacionNpo(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = AsignacionNpoForm
    # template_name = 'asignacion_npo/create_asignacion_npo.html'
    template_name = 'asignacion_npo/includes/partials/create_asignacion_npo_modal.html'
    # success_url = reverse_lazy('asignaciones:detail_asignacion')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.npo_asignador = self.request.user.perfil
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        npo_ingeniero = form.cleaned_data['npo_ingeniero']
        fm_supervisor = form.cleaned_data['fm_supervisor']
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        try:
            form.instance.npo_ingeniero_celular = npo_ingeniero.celular
        except Exception:
            pass
        try:
            form.instance.npo_ingeniero_empresa = npo_ingeniero.empresa
        except Exception:
            pass
        try:
            form.instance.fm_supervisor_celular = fm_supervisor.celular
        except Exception:
            pass
        try:
            form.instance.fm_supervisor_empresa = fm_supervisor.empresa
        except Exception:
            pass
        return super(CreateAsignacionNpo, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateAsignacionNpo, self).get_form_kwargs()
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        npo_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'npo_asignador': npo_asignador})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateAsignacionNpo, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(pk=self.kwargs['pk'])
        return context

class ListAsignacionNpo(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    template_name = 'asignacion_npo/list_asignacion_npo.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        qs = self.request.GET.get('qs')
        print (qs)
        if qs and qs == 'asignaciones_npo_asignada_previo_hoy_qs':
            queryset = asignaciones_npo_asignada_previo_hoy_qs()
        if qs and qs == 'asignaciones_npo_en_monitoreo_tres_dias_qs':
            queryset = asignaciones_npo_en_monitoreo_tres_dias_qs()
        return queryset

class ListAsignacionNpoActividad(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListAsignacionNpoPerfil(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ASIGNADA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoA(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ASIGNADA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoB(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = EN_MONITOREO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoC(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ENVIADO_A_SEGUIMIENTO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoD(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = REQUIERE_VISITA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoE(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = NO_EXITOSA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoEstadoF(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ESCALADO_A_CLARO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoHoy(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = datetime.date.today()
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(fecha_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(fecha_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(fecha_asignacion=query, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(fecha_asignacion=query, npo_ingeniero=perfil)
        return queryset

class ListAsignacionNpoFecha(ListAsignacionNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNpo, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        estado_asignacion = self.request.GET.get('estado_asignacion')
        query = self.request.GET.get('fecha')
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(fecha_asignacion=query, estado_asignacion=estado_asignacion)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(fecha_asignacion=query, estado_asignacion=estado_asignacion, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_ASIGNADOR:
            queryset = queryset.filter(fecha_asignacion=query, estado_asignacion=estado_asignacion, npo_asignador=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(fecha_asignacion=query, estado_asignacion=estado_asignacion, npo_ingeniero=perfil)
        return queryset

class SearchAsignacionNpo(ListAsignacionNpo):

    def get_queryset(self):
        queryset = super(SearchAsignacionNpo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_asignador__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_asignador__apellido__icontains=q) for q in query_list)) |
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
                          (Q(estado_asignacion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_intervencion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

class DetailAsignacionNpo(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    template_name = 'asignacion_npo/detail_asignacion_npo.html'

class UpdateAsignacionNpo(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    form_class = AsignacionNpoForm
    # template_name = 'asignacion_npo/update_asignacion_npo.html'
    template_name = 'asignacion_npo/includes/partials/update_asignacion_npo_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_npo_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super(UpdateAsignacionNpo, self).get_form_kwargs()
        actividad = self.object.actividad
        npo_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'npo_asignador': npo_asignador})
        return kwargs

class UpdateAsignacionNpoAsiganador(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    form_class = AsignacionNpoAsiganadorForm
    # template_name = 'asignacion_npo/update_asignacion_npo.html'
    template_name = 'asignacion_npo/includes/partials/update_asignacion_npo_asignador_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_npo_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()
    def get_form_kwargs(self):
        kwargs = super(UpdateAsignacionNpoAsiganador, self).get_form_kwargs()
        actividad = self.object.actividad
        npo_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'npo_asignador': npo_asignador})
        return kwargs

class UpdateAsignacionNpoIngeniero(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    form_class = AsignacionNpoIngenieroForm
    # template_name = 'asignacion_npo/update_asignacion_npo.html'
    template_name = 'asignacion_npo/includes/partials/update_asignacion_npo_ingeniero_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_npo_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

class DeleteAsignacionNpo(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = AsignacionNpo
    template_name = 'asignacion_npo/delete_asignacion_npo.html'
    success_url = reverse_lazy('asignaciones:list_asignacion_npo')

def export_asignaciones_npo(request):
    asignaciones_npo_resource = AsignacionNpoResource()
    user = request.user
    queryset = AsignacionNpo.objects.filter(npo_asignador=user.perfil.id)
    dataset = asignaciones_npo_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AsignacionNpo.xlsx"'
    return response

class CreateAsignacionNi(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = AsignacionNiForm
    # template_name = 'asignacion_ni/create_asignacion_ni.html'
    template_name = 'asignacion_ni/includes/partials/create_asignacion_ni_modal.html'
    success_url = reverse_lazy('actividades:list_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.ni_asignador = self.request.user.perfil
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        ni_ingeniero = form.cleaned_data['ni_ingeniero']
        fm_supervisor = form.cleaned_data['fm_supervisor']
        asignar_par = form.cleaned_data['asignar_par']
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        try:
            form.instance.ni_ingeniero_celular = ni_ingeniero.celular
        except Exception:
            pass
        try:
            form.instance.ni_ingeniero_empresa = ni_ingeniero.empresa
        except Exception:
            pass
        try:
            form.instance.fm_supervisor_celular = fm_supervisor.celular
        except Exception:
            pass
        try:
            form.instance.fm_supervisor_empresa = fm_supervisor.empresa
        except Exception:
            pass
        if asignar_par:
            AsignacionNpo.objects.create(
                npo_asignador=self.request.user.perfil,
                npo_ingeniero=ni_ingeniero.par.perfil,
                estacion=actividad.estacion,
                actividad=actividad,
                wp=actividad.wp,
                tipo_intervencion=form.instance.tipo_intervencion,
                fecha_asignacion=form.instance.fecha_asignacion
            )
        return super(CreateAsignacionNi, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateAsignacionNi, self).get_form_kwargs()
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        ni_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'ni_asignador': ni_asignador})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateAsignacionNi, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(pk=self.kwargs['pk'])
        return context

class ListAsignacionNi(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = AsignacionNi
    template_name = 'asignacion_ni/list_asignacion_ni.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        qs = self.request.GET.get('qs')
        print (qs)
        if qs and qs == 'asignaciones_ni_asignada_previo_hoy_qs':
            queryset = asignaciones_ni_asignada_previo_hoy_qs()
        if qs and qs == 'asignaciones_ni_en_monitoreo_tres_dias_qs':
            queryset = asignaciones_ni_en_monitoreo_tres_dias_qs()
        return queryset

class ListAsignacionNiActividad(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListAsignacionNiPerfil(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ASIGNADA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoA(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ASIGNADA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoB(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = EN_MONITOREO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoC(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ENVIADO_A_SEGUIMIENTO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoD(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = REQUIERE_VISITA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoE(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = NO_EXITOSA
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiEstadoF(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = ESCALADO_A_CLARO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(estado_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiHoy(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        query = datetime.date.today()
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(fecha_asignacion=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(fecha_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(fecha_asignacion=query, ni_asignador=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(fecha_asignacion=query, ni_ingeniero=perfil)
        return queryset

class ListAsignacionNiFecha(ListAsignacionNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListAsignacionNi, self).get_queryset()
        perfil = Perfil.objects.get(slug=self.kwargs['slug'])
        estado_asignacion = self.request.GET.get('estado_asignacion')
        query = self.request.GET.get('fecha')
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(fecha_asignacion=query, estado_asignacion=estado_asignacion)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(fecha_asignacion=query, ni_asignador=perfil, estado_asignacion=estado_asignacion)
        if query and perfil.perfil_usuario == NI_ASIGNADOR:
            queryset = queryset.filter(fecha_asignacion=query, ni_asignador=perfil, estado_asignacion=estado_asignacion)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(fecha_asignacion=query, ni_ingeniero=perfil, estado_asignacion=estado_asignacion)
        return queryset

class SearchAsignacionNi(ListAsignacionNi):

    def get_queryset(self):
        queryset = super(SearchAsignacionNi, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_asignador__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_asignador__apellido__icontains=q) for q in query_list)) |
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
                          (Q(estado_asignacion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_intervencion__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

class DetailAsignacionNi(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = AsignacionNi
    template_name = 'asignacion_ni/detail_asignacion_ni.html'

class UpdateAsignacionNi(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNi
    form_class = AsignacionNiForm
    # template_name = 'asignacion_ni/update_asignacion_ni.html'
    template_name = 'asignacion_ni/includes/partials/update_asignacion_ni_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_ni_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super(UpdateAsignacionNi, self).get_form_kwargs()
        actividad = self.object.actividad
        ni_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'ni_asignador': ni_asignador})
        return kwargs

class UpdateAsignacionNiAsignador(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNi
    form_class = AsignacionNiAsignadorForm
    # template_name = 'asignacion_ni/update_asignacion_ni.html'
    template_name = 'asignacion_ni/includes/partials/update_asignacion_ni_asignador_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_ni_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        actividad = self.object.actividad
        ni_ingeniero = form.cleaned_data['ni_ingeniero']
        asignar_par = form.cleaned_data['asignar_par']
        if asignar_par:
            AsignacionNpo.objects.create(
                npo_asignador=self.request.user.perfil,
                npo_ingeniero=ni_ingeniero.par.perfil,
                estacion=actividad.estacion,
                actividad=actividad,
                wp=actividad.wp,
                tipo_intervencion=form.instance.tipo_intervencion,
                fecha_asignacion=form.instance.fecha_asignacion
            )
        return super(UpdateAsignacionNiAsignador, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UpdateAsignacionNiAsignador, self).get_form_kwargs()
        actividad = self.object.actividad
        ni_asignador = Perfil.objects.get(user=self.request.user)
        kwargs.update({'actividad': actividad})
        kwargs.update({'ni_asignador': ni_asignador})
        return kwargs

class UpdateAsignacionNiIngeniero(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = AsignacionNi
    form_class = AsignacionNiIngenieroForm
    # template_name = 'asignacion_ni/update_asignacion_ni.html'
    template_name = 'asignacion_ni/includes/partials/update_asignacion_ni_ingeniero_modal.html'
    # success_url = reverse_lazy('asignaciones:list_asignacion_ni_perfil')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

class DeleteAsignacionNi(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = AsignacionNi
    template_name = 'asignacion_ni/delete_asignacion_ni.html'
    success_url = reverse_lazy('asignaciones:list_asignacion_ni')

def export_asignaciones_ni(request):
    asignaciones_ni_resource = AsignacionNiResource()
    user = request.user
    queryset = AsignacionNi.objects.filter(ni_asignador=user.perfil.id)
    dataset = asignaciones_ni_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AsignacionNi.xlsx"'
    return response
