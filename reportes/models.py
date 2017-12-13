# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from users.models import Perfil

class ReporteActividad(models.Model):
    gap_administrador = models.ManyToManyField(Perfil)
    # de actividad
    wp = models.IntegerField(blank=True, null=True)
    agrupador = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.CharField(max_length=255, blank=True, null=True)
    regional = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    banda = models.CharField(max_length=255, blank=True, null=True)
    valor_wp_eur = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, editable=False)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    fecha_integracion = models.DateField(blank=True, null=True)
    grupo_gap = models.CharField(max_length=255, blank=True, null=True)
    tipo_trabajo_noc = models.CharField(max_length=255, blank=True, null=True)
    estado_noc = models.CharField(max_length=255, blank=True, null=True)
    subestado_noc = models.CharField(max_length=255, blank=True, null=True)
    # de asignaciones ni
    responsable_ni = models.CharField(max_length=255, blank=True, null=True)
    estado_ni = models.CharField(max_length=255, blank=True, null=True)
    concepto_ni = models.TextField(blank=True, null=True)
    tipo_intervencion_ni = models.CharField(max_length=255, blank=True, null=True)
    fecha_asignacion_ni = models.DateField(blank=True, null=True)
    # de actividad
    requiere_hw = models.CharField(max_length=255, blank=True, null=True)
    responsable_actual = models.CharField(max_length=255, blank=True, null=True)
    # de asignaciones npo
    responsable_npo = models.CharField(max_length=255, blank=True, null=True)
    estado_npo = models.CharField(max_length=255, blank=True, null=True)
    posible_causa = models.CharField(max_length=255, blank=True, null=True)
    concepto_npo = models.TextField(blank=True, null=True)
    tipo_intervencion_npo = models.CharField(max_length=255, blank=True, null=True)
    fecha_asignacion_npo = models.DateField(blank=True, null=True)
    # de actividad
    supervisor = models.CharField(max_length=255, blank=True, null=True)
    fecha_fc_visita = models.DateField(blank=True, null=True)
    id_siteaccess = models.CharField(max_length=255, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "reporte actividad"
        verbose_name_plural = "reporte actividades"

    def __str__(self):
        return str(self.creado.strftime('%d/%m/%y'))

    def get_absolute_url(self):
        return reverse('reportes:list_reporte_actividad')
