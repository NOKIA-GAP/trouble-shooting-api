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
ComentarioNpoForm,
ComentarioNiForm,
)
from .models import (
ComentarioNpo,
ComentarioNi,
)
import operator
from django.db.models import Q
from functools import reduce
from .resources import ComentarioNpoResource, ComentarioNiResource
from django.http import HttpResponse
from incidentes.models import IncidenteNpo, IncidenteNi
from actividades.models import Actividad

class CreateComentarioNpo(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ComentarioNpoForm
    # template_name = 'comentario_npo/create_comentario_npo.html'
    template_name = 'comentario_npo/includes/partials/create_comentario_npo.html'
    # success_url = reverse_lazy('actividades:detail_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.npo_ingeniero = self.request.user.perfil
        incidente = IncidenteNpo.objects.get(pk=self.kwargs['pk'])
        form.instance.incidente_npo = incidente
        actividad = incidente.actividad
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateComentarioNpo, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateComentarioNpo, self).get_context_data(**kwargs)
        context['incidente_npo'] = IncidenteNpo.objects.get(pk=self.kwargs['pk'])
        return context

class ListComentarioNpo(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = ComentarioNpo
    template_name = 'comentario_npo/list_comentario_npo.html'
    paginate_by = 100

class ListComentarioNpoActividad(ListComentarioNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListComentarioNpo, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListComentarioNpoIncidente(ListComentarioNpo):

    def get_queryset(self, **kwargs):
        queryset = super(ListComentarioNpo, self).get_queryset()
        query = IncidenteNpo.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(incidente_npo_id=query)
        return queryset

class DetailComentarioNpo(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = ComentarioNpo
    template_name = 'comentario_npo/detail_comentario_npo.html'

class UpdateComentarioNpo(LoginRequiredMixin, UpdateView,):
    login_url = 'users:login_user'
    model = ComentarioNpo
    form_class = ComentarioNpoForm
    # template_name = 'comentario_npo/update_comentario_npo.html'
    template_name = 'comentario_npo/includes/partials/update_comentario_npo.html'
    # success_url = reverse_lazy('comentarios:detail_comentario_npo')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateComentarioNpo, self).get_context_data(**kwargs)
        context['incidente_npo'] = self.object.incidente_npo
        return context


class DeleteComentarioNpo(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = ComentarioNpo
    # template_name = 'comentario_npo/delete_comentario_npo.html'
    template_name = 'comentario_npo/includes/partials/delete_comentario_npo.html'
    # success_url = reverse_lazy('comentarios:list_comentario_ni_incidente')

    def get_context_data(self, **kwargs):
        context = super(DeleteComentarioNpo, self).get_context_data(**kwargs)
        context['incidente_npo'] = self.object.incidente_npo
        return context

    def get_success_url(self):
        incidente_npo = self.object.incidente_npo
        return reverse_lazy( 'comentarios:list_comentario_npo_incidente', kwargs={'pk': incidente_npo.pk})

class SearchComentarioNpo(ListComentarioNpo):

    def get_queryset(self):
        queryset = super(SearchComentarioNpo, self).get_queryset()
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
                          (Q(npo_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
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

def export_comentarios_npo(request):
    comentarios_npo_resource = ComentarioNpoResource()
    dataset = comentarios_npo_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ComentarioNpo.xlsx"'
    return response

class CreateComentarioNi(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ComentarioNiForm
    # template_name = 'comentario_ni/create_comentario_ni.html'
    template_name = 'comentario_ni/includes/partials/create_comentario_ni.html'
    # success_url = reverse_lazy('actividades:detail_actividad')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.ni_ingeniero = self.request.user.perfil
        incidente = IncidenteNi.objects.get(pk=self.kwargs['pk'])
        form.instance.incidente_ni = incidente
        actividad = incidente.actividad
        form.instance.estacion = actividad.estacion
        form.instance.actividad = actividad
        form.instance.wp = actividad.wp
        return super(CreateComentarioNi, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateComentarioNi, self).get_context_data(**kwargs)
        context['incidente_ni'] = IncidenteNi.objects.get(pk=self.kwargs['pk'])
        return context



class ListComentarioNi(LoginRequiredMixin, ListView):
    login_url = 'login_user'
    model = ComentarioNi
    template_name = 'comentario_ni/list_comentario_ni.html'
    paginate_by = 100

class ListComentarioNiActividad(ListComentarioNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListComentarioNi, self).get_queryset()
        query = Actividad.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(actividad_id=query)
        return queryset

class ListComentarioNiIncidente(ListComentarioNi):

    def get_queryset(self, **kwargs):
        queryset = super(ListComentarioNi, self).get_queryset()
        query = IncidenteNi.objects.get(pk=self.kwargs['pk'])
        if query:
            queryset = queryset.filter(incidente_ni_id=query)
        return queryset

class DetailComentarioNi(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = ComentarioNi
    template_name = 'comentario_ni/detail_comentario_ni.html'

class UpdateComentarioNi(LoginRequiredMixin, UpdateView,):
    login_url = 'login_user'
    model = ComentarioNi
    form_class = ComentarioNiForm
    # template_name = 'comentario_ni/update_comentario_ni.html'
    template_name = 'comentario_ni/includes/partials/update_comentario_ni.html'
    # success_url = reverse_lazy('comentarios:detail_comentario_ni')

    # def get_success_url(self, **kwargs):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateComentarioNi, self).get_context_data(**kwargs)
        context['incidente_ni'] = self.object.incidente_ni
        return context

class DeleteComentarioNi(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = ComentarioNi
    # template_name = 'comentario_ni/delete_comentario_ni.html'
    template_name = 'comentario_ni/includes/partials/delete_comentario_ni.html'
    # success_url = reverse_lazy('comentarios:list_comentario_ni')

    def get_context_data(self, **kwargs):
        context = super(DeleteComentarioNi, self).get_context_data(**kwargs)
        context['incidente_ni'] = self.object.incidente_ni
        return context

    def get_success_url(self):
        incidente_ni = self.object.incidente_ni
        return reverse_lazy( 'comentarios:list_comentario_ni_incidente', kwargs={'pk': incidente_ni.pk})


class SearchComentarioNi(ListComentarioNi):

    def get_queryset(self):
        queryset = super(SearchComentarioNi, self).get_queryset()
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
                          (Q(ni_ingeniero__nombre_completo__icontains=q) for q in query_list)) |
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

def export_comentarios_ni(request):
    comentarios_ni_resource = ComentarioNiResource()
    dataset = comentarios_ni_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ComentarioNi.xlsx"'
    return response
