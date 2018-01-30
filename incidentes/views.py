from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView
)
from django.urls import reverse_lazy
from .forms import (
IncidenteNpoForm,
IncidenteIngenieroNpoForm,
IncidenteNiForm,
IncidenteIngenieroNiForm,

)
from .models import (
IncidenteNpo,
IncidenteNi,
)
import operator
from django.db.models import Q
from functools import reduce
from .resources import IncidenteNpoResource, IncidenteNiResource
from django.http import HttpResponse
from actividades.models import Actividad
from users.models import Perfil

GAP_ADMINISTRADOR = 'GAP Administrador'
NI_INGENIERO = 'NI Ingeniero'
NPO_INGENIERO = 'NPO Ingeniero'
FM_LIDER = 'FM Lider'
ABIERTO = 'Abierto'
CERRADO = 'Cerrado'

class CreateIncidenteNpo(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = IncidenteNpoForm
    template_name = 'incidente_npo/includes/partials/create_incidente_npo.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIncidenteNpo, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super(CreateIncidenteNpo, self).get_form_kwargs()
        asignador = Perfil.objects.get(user=self.request.user)
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        kwargs.update({'actividad': actividad})
        kwargs.update({'asignador': asignador})
        return kwargs

    def form_valid(self, form):
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        npo_ingeniero = form.cleaned_data['npo_ingeniero']
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateIncidenteNpo, self).form_valid(form)

class ListIncidenteNpo(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = IncidenteNpo
    template_name = 'incidente_npo/list_incidente_npo.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListIncidenteNpo, self).get_queryset()
        perfil = self.request.user.perfil
        query = ABIERTO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_incidente=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        return queryset

class ListIncidenteCerradoNpo(ListIncidenteNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListIncidenteNpo, self).get_queryset()
        perfil = self.request.user.perfil
        query = CERRADO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_incidente=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, npo_ingeniero=perfil)
        return queryset

class SearchIncidenteNpo(ListIncidenteNpo):

    def get_queryset(self):
        queryset = super(ListIncidenteNpo, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(npo_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_incidente__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

class DetailIncidenteNpo(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = IncidenteNpo
    template_name = 'incidente_npo/detail_incidente_npo.html'

class UpdateIncidenteNpo(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = IncidenteNpo
    form_class = IncidenteNpoForm
    template_name = 'incidente_npo/includes/partials/update_incidente_npo.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateIncidenteNpo, self).get_context_data(**kwargs)
        context['actividad'] = self.object.actividad
        return context

class UpdateIncidenteIngenieroNpo(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = IncidenteNpo
    form_class = IncidenteIngenieroNpoForm
    template_name = 'incidente_npo/includes/partials/update_incidente_ingeniero_npo.html'

class CreateIncidenteNi(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = IncidenteNiForm
    template_name = 'incidente_ni/includes/partials/create_incidente_ni.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIncidenteNi, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super(CreateIncidenteNi, self).get_form_kwargs()
        asignador = Perfil.objects.get(user=self.request.user)
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        kwargs.update({'actividad': actividad})
        kwargs.update({'asignador': asignador})
        return kwargs

    def form_valid(self, form):
        actividad = Actividad.objects.get(pk=self.kwargs['pk'])
        ni_ingeniero = form.cleaned_data['ni_ingeniero']
        asignar_par = form.cleaned_data['asignar_par']
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        if asignar_par:
            IncidenteNpo.objects.create(
                estacion=actividad.estacion,
                actividad=actividad,
                wp=actividad.wp,
                npo_ingeniero=ni_ingeniero.par.perfil,
            )
        return super(CreateIncidenteNi, self).form_valid(form)

class ListIncidenteNi(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = IncidenteNi
    template_name = 'incidente_ni/list_incidente_ni.html'
    paginate_by = 100

    def get_queryset(self, **kwargs):
        queryset = super(ListIncidenteNi, self).get_queryset()
        perfil = self.request.user.perfil
        query = ABIERTO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_incidente=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        return queryset

class ListIncidenteCerradoNi(ListIncidenteNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListIncidenteNi, self).get_queryset()
        perfil = self.request.user.perfil
        query = CERRADO
        if query and perfil.perfil_usuario == GAP_ADMINISTRADOR:
            queryset = queryset.filter(estado_incidente=query)
        if query and perfil.perfil_usuario == FM_LIDER:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        if query and perfil.perfil_usuario == NI_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        if query and perfil.perfil_usuario == NPO_INGENIERO:
            queryset = queryset.filter(estado_incidente=query, ni_ingeniero=perfil)
        return queryset

class SearchIncidenteNi(ListIncidenteNi):

    def get_queryset(self):
        queryset = super(ListIncidenteNi, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                          (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estacion__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actividad__id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(wp__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__apellido__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_incidente__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

class DetailIncidenteNi(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = IncidenteNi
    template_name = 'incidente_ni/detail_incidente_ni.html'

class UpdateIncidenteNi(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = IncidenteNi
    form_class = IncidenteNiForm
    template_name = 'incidente_ni/includes/partials/update_incidente_ni.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateIncidenteNi, self).get_context_data(**kwargs)
        context['actividad'] = self.object.actividad
        return context

class UpdateIncidenteIngenieroNi(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = IncidenteNi
    form_class = IncidenteIngenieroNiForm
    template_name = 'incidente_ni/includes/partials/update_incidente_ingeniero_ni.html'
