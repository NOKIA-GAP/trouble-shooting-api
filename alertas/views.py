from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
ListView,
DetailView,
UpdateView,
DeleteView,
)
from django.urls import reverse_lazy
from .models import Alerta
from .forms import AlertaForm
import operator
from django.db.models import Q
from functools import reduce

class ListAlerta(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = Alerta
    template_name = 'alerta/list_alerta.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(ListAlerta, self).get_context_data(**kwargs)
        context['alertas_count'] = self.get_queryset().count()
        return context

class SearchAlerta(ListAlerta):

    def get_queryset(self):
        queryset = super(ListAlerta, self).get_queryset()
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
                          (Q(mensaje__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(estado_alerta__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(tipo_alerta__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(creado__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                          (Q(actualizado__icontains=q) for q in query_list))
            )
        return queryset

class DetailAlerta(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Alerta
    template_name = 'alerta/detail_alerta.html'

class UpdateAlerta(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = Alerta
    form_class = AlertaForm
    template_name = 'alerta/includes/partials/update_alerta.html'

class DeleteAlerta(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = Alerta
    template_name = 'alerta/includes/partials/delete_alerta.html'

    def get_success_url(self):
        return reverse_lazy('alertas:list_alerta')
