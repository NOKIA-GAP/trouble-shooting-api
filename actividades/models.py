# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from estaciones.models import Estacion
from . import choices
from django.contrib.auth.models import User
from users.models import Perfil

PRODUCCION = 'Produccion'


class Actividad(models.Model):
    wp = models.BigIntegerField(blank=True, null=True, unique=True)#campo no editable
    id_notificacion_noc = models.IntegerField(blank=True, null=True)
    agrupador = models.CharField(max_length=255, blank=True, null=True)#campo no editable
    service_supplier = models.CharField(max_length=255, blank=True, choices=choices.SERVICE_SUPPLIER_CHOICES, null=True)#campo no editable
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE,  blank=True, null=True, related_name='actividades')#campo no editable
    banda = models.CharField(max_length=255, blank=True, null=True)#campo no editable
    valor_wp_eur = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)#campo no editable
    proyecto = models.CharField(max_length=255, blank=True, null=True)#campo no editable
    escenario = models.CharField(max_length=255, blank=True, null=True)#campo no editable
    tipo_trabajo = models.CharField(max_length=255, choices=choices.TIPO_TRABAJO_CHOICES, blank=True, null=True)
    fecha_ingreso_onair = models.DateField(blank=True, null=True)
    realtifinish = models.DateField(blank=True, null=True)
    fecha_integracion = models.DateField(blank=True, null=True)
    grupo_gap = models.CharField(max_length=255, choices=choices.GRUPO_GAP_CHOICES, blank=True, null=True)
    ss_tbs = models.CharField(max_length=255, choices=choices.SS_TBS_CHOICES, blank=True, null=True)
    po_solicitud = models.DateField(blank=True, null=True)
    fecha_estado_noc = models.DateField(blank=True, null=True)
    estado_noc = models.CharField(max_length=255, choices=choices.ESTADO_NOC_CHOICES, blank=True, null=True)
    subestado_noc = models.CharField(max_length=255, choices=choices.SUBESTADO_NOC_CHOICES, blank=True, null=True)
    impacto_degradacion = models.CharField(max_length=255, choices=choices.IMPACTO_DEGRADACION_CHOICES, blank=True, null=True)
    fecha_fc_visita = models.DateField(blank=True, null=True)
    requiere_hw = models.CharField(max_length=255, choices=choices.REQUIERE_HW_CHOICES, blank=True, null=True)
    cantidad_hw = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    # Extra fields

    # asignaciones npo
    npo_ingeniero = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_estado_asignacion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_posible_causa = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_concepto = models.TextField(blank=True, null=True, editable=False)
    npo_tipo_intervencion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_fecha_asignacion = models.DateField(blank=True, null=True, editable=False)
    npo_fm_supervisor = models.CharField(max_length=255, blank=True, null=True, editable=False)
    # asignaciones ni
    ni_ingeniero = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_estado_asignacion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_concepto = models.TextField(blank=True, null=True, editable=False)
    ni_estado_solicitud_hw = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_tipo_intervencion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_fecha_asignacion = models.DateField(blank=True, null=True, editable=False)
    ni_fm_supervisor = models.CharField(max_length=255, blank=True, null=True, editable=False)

    # asignaciones npo y asignaciones ni
    estado_ultimo = models.CharField(max_length=255, blank=True, null=True, editable=False)
    estado_unico = models.CharField(max_length=255, blank=True, null=True, editable=False)

    class Meta:
        ordering = ('creado',)
        verbose_name = "actividad"
        verbose_name_plural = "actividades"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('actividades:detail_actividad', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.grupo_gap == None and self.estado_noc == PRODUCCION:
            self.grupo_gap = self.estacion.responsable
        super(Actividad, self).save(*args, **kwargs)


class Degradacion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='degradaciones')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='degradaciones')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='degradaciones')
    wp = models.BigIntegerField(blank=True, null=True)
    contenido= models.TextField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "degradacion"
        verbose_name_plural = "degradaciones"

    def __str__(self):
        return str(self.id)

    # def __str__(self):
    #     return str(self.creado.strftime('%d/%m/%y'))

    def get_absolute_url(self):
        return reverse('actividades:detail_degradacion', kwargs={'pk': self.pk})
