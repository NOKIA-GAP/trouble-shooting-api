# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
TemplateView,
FormView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView
)
from django.urls import reverse_lazy
from .forms import (
ReporteActividadForm
)
from .models import ReporteActividad
from actividades.models import Actividad
import operator
from django.db.models import Q
from functools import reduce
from .resources import ReporteActividadResource
from django.http import HttpResponse

class ListReporteActividad(LoginRequiredMixin, ListView):
    login_url = 'users:login_user'
    model = ReporteActividad
    template_name = 'reporte_actividad/list_reporte_actividad.html'
    paginate_by = 100


class CreateReporteActividad(LoginRequiredMixin, CreateView):
    login_url = 'users:login_user'
    form_class = ReporteActividadForm
    template_name = 'reporte_actividad/create_reporte_actividad.html'
    success_url = reverse_lazy('reportes:list_reporte_actividad')

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        actividades = Actividad.objects.all()
        objs = []

        for actividad in actividades:
            reporte_actividad = ReporteActividad()
            # de actividad
            reporte_actividad.wp = actividad.wp
            reporte_actividad.agrupador = actividad.agrupador
            reporte_actividad.estacion = actividad.estacion.nombre
            reporte_actividad.regional = actividad.estacion.regional
            reporte_actividad.ciudad = actividad.estacion.ciudad
            reporte_actividad.banda = actividad.banda
            reporte_actividad.valor_wp_eur = actividad.valor_wp_eur
            reporte_actividad.proyecto = actividad.proyecto
            reporte_actividad.escenario = actividad.escenario
            reporte_actividad.fecha_integracion = actividad.fecha_integracion
            reporte_actividad.grupo_gap = actividad.grupo_gap
            reporte_actividad.tipo_trabajo_noc = actividad.tipo_trabajo
            reporte_actividad.estado_noc = actividad.estado_noc
            reporte_actividad.subestado_noc = actividad.subestado_noc
            # de asignaciones ni
            try:
                asignacion_ni = actividad.asignaciones_ni.last()
                reporte_actividad.responsable_ni = asignacion_ni.ni_ingeniero
                reporte_actividad.estado_ni = asignacion_ni.estado
                reporte_actividad.tipo_intervencion_ni = asignacion_ni.tipo_intervencion
                reporte_actividad.fecha_asignacion_ni = asignacion_ni.fecha_asignacion
                try:
                    concepto_ni = asignacion_ni.conceptos_ni.last()
                    reporte_actividad.concepto_ni = concepto_ni.contenido
                except:
                    pass
            except:
                pass
            # de actividad
            reporte_actividad.requiere_hw = actividad.requiere_hw
            reporte_actividad.responsable_actual = actividad.responsable_actual
            # de asignaciones npo
            try:
                asignacion_npo = actividad.asignaciones_npo.last()
                reporte_actividad.responsable_npo = asignacion_npo.npo_ingeniero
                reporte_actividad.estado_npo = asignacion_npo.estado
                reporte_actividad.posible_causa = asignacion_npo.posible_causa
                reporte_actividad.tipo_intervencion_npo = asignacion_npo.tipo_intervencion
                reporte_actividad.fecha_asignacion_npo = asignacion_npo.fecha_asignacion
                try:
                    concepto_npo = asignacion_npo.conceptos_npo.last()
                    reporte_actividad.concepto_npo = concepto_npo.contenido
                except:
                    pass
            except:
                pass
            # de actividad
            reporte_actividad.supervisor = actividad.visita_supervisor
            reporte_actividad.fecha_fc_visita = actividad.fecha_fc_visita
            reporte_actividad.id_siteaccess = actividad.id_siteaccess
            objs.append(reporte_actividad)

        ReporteActividad.objects.bulk_create(objs)

        # form.send_email()
        # form.export_reporte_actividad()
        # form.delete_reporte_actividad()
        return super(CreateReporteActividad, self).form_valid(form)


def export_reporte_actividad(request):
    reporte_actividad_resource = ReporteActividadResource()
    dataset = reporte_actividad_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ReporteActividad.xlsx"'
    return response

class DetailReporteActividad(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = ReporteActividad
    template_name = 'reporte_actividad/detail_reporte_actividad.html'

class DeleteReporteActividad(LoginRequiredMixin, DeleteView):
    login_url = 'users:login_user'
    model = ReporteActividad
    template_name = 'reporte_actividad/reporte_actividad.html'
    success_url = reverse_lazy('actividades:list_actividad')
