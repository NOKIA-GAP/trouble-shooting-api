# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from estaciones.models import Estacion
from . import choices
from django.contrib.auth.models import User
from users.models import Perfil

from django.db.models.signals import post_save
from django.dispatch import receiver

ASIGNADA = 'Asignada'
REQUIERE_VISITA = 'Requiere visita'
EN_MONITOREO = 'En monitoreo'
ESCALADO_A_CLARO = 'Escalado a claro'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
PRODUCCION = 'Produccion'


class Actividad(models.Model):
    wp = models.BigIntegerField(blank=True, null=True, unique=True)
    id_notificacion_noc = models.IntegerField(blank=True, null=True)
    agrupador = models.CharField(max_length=255, blank=True, null=True)
    service_supplier = models.CharField(max_length=255, blank=True, choices=choices.SERVICE_SUPPLIER_CHOICES, null=True)
    field_manager = models.CharField(max_length=255, blank=True, null=True)
    valor_wp_eur = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE,  blank=True, null=True, related_name='actividades')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    tipo_trabajo = models.CharField(max_length=255, choices=choices.TIPO_TRABAJO_CHOICES, blank=True, null=True)
    fecha_ingreso_onair = models.DateField(blank=True, null=True)
    realtifinish = models.DateField(blank=True, null=True)
    fecha_integracion = models.DateField(blank=True, null=True)
    grupo_gap = models.CharField(max_length=255, choices=choices.GRUPO_GAP_CHOICES, blank=True, null=True)
    fecha_estado_noc = models.DateField(blank=True, null=True)
    estado_noc = models.CharField(max_length=255, choices=choices.ESTADO_NOC_CHOICES, blank=True, null=True)
    subestado_noc = models.CharField(max_length=255, choices=choices.SUBESTADO_NOC_CHOICES, blank=True, null=True)
    impacto_degradacion = models.CharField(max_length=255, choices=choices.IMPACTO_DEGRADACION_CHOICES, blank=True, null=True)
    fecha_fc_visita = models.DateField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    # Extra fields

    # asignaciones npo
    npo_ingeniero = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_estado_asignacion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_concepto = models.TextField(blank=True, null=True, editable=False)
    npo_tipo_intervencion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    npo_fecha_asignacion = models.DateField(blank=True, null=True, editable=False)
    npo_fm_supervisor = models.CharField(max_length=255, blank=True, null=True, editable=False)
    # asignaciones ni
    ni_ingeniero = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_estado_asignacion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_origen_falla = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_solver = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_concepto = models.TextField(blank=True, null=True, editable=False)
    ni_estado_solicitud_hw = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_tipo_intervencion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    ni_fecha_asignacion = models.DateField(blank=True, null=True, editable=False)
    ni_fm_supervisor = models.CharField(max_length=255, blank=True, null=True, editable=False)
    clasificacion_previa = models.CharField(max_length=255, blank=True, null=True, editable=False)

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
        if self.estado_noc == PRODUCCION:
            self.estado_unico = PRODUCCION

        estacion = self.estacion
        actividades = estacion.actividades.all()
        try:
            produccion = actividades.filter(estado_unico=PRODUCCION)
            if produccion:
                estacion.estado_estacion = PRODUCCION

            enviado_a_seguimiento = actividades.filter(estado_unico=ENVIADO_A_SEGUIMIENTO)
            if enviado_a_seguimiento:
                estacion.estado_estacion = ENVIADO_A_SEGUIMIENTO

            escalado_a_claro = actividades.filter(estado_unico=ESCALADO_A_CLARO)
            if escalado_a_claro:
                estacion.estado_estacion = ESCALADO_A_CLARO

            en_monitoreo = actividades.filter(estado_unico=EN_MONITOREO)
            if en_monitoreo:
                estacion.estado_estacion = EN_MONITOREO

            requiere_visita = actividades.filter(estado_unico=REQUIERE_VISITA)
            if requiere_visita:
                estacion.estado_estacion = REQUIERE_VISITA

            asignada = actividades.filter(estado_unico=ASIGNADA)
            if asignada:
                estacion.estado_estacion = ASIGNADA
            estacion.numero_actividades = actividades.count()
            estacion.save()
        except Exception:
            pass
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
