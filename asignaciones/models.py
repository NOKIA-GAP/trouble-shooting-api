# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Perfil
from estaciones.models import Estacion
from actividades.models import Actividad
from . import choices
from django.db.models.signals import post_save
from django.dispatch import receiver

PRODUCCION = 'Produccion'

ASIGNADA = 'Asignada'
EN_MONITOREO = 'En monitoreo'
ENVIADO_A_SEGUIMIENTO = 'Enviado a seguimiento'
REQUIERE_VISITA = 'Requiere visita'
NO_EXITOSA = 'No exitosa'
ESCALADO_A_CLARO = 'Escalado a claro'

class AsignacionNpo(models.Model):
    npo_asignador = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_npo_asignador')
    npo_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_npo_ingeniero')
    npo_ingeniero_celular = models.CharField(max_length=255, blank=True, null=True)
    npo_ingeniero_empresa = models.CharField(max_length=255, blank=True, null=True)
    fm_supervisor = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_npo_fm_supervisor')
    fm_supervisor_celular = models.CharField(max_length=255, blank=True, null=True)
    fm_supervisor_empresa = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_npo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_npo')
    wp = models.BigIntegerField(blank=True, null=True)
    estado_asignacion = models.CharField(max_length=255, choices=choices.ESTADO_ASIGNACION_CHOICES, default='Asignada', blank=True, null=True)
    tipo_intervencion = models.CharField(max_length=255, choices=choices.TIPO_INTERVENCION_CHOICES, blank=True, null=True)
    fecha_asignacion = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    # Extra fields

    # conceptos npo
    npo_concepto = models.TextField(blank=True, null=True, editable=False)

    class Meta:
        ordering = ('creado',)
        verbose_name = "asignacion npo"
        verbose_name_plural = "asignaciones npo"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('asignaciones:detail_asignacion_npo', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        _actividad = Actividad.objects.get(id=self.actividad.id)

        # asignaciones npo
        try:
            _actividad.npo_ingeniero = self.npo_ingeniero.nombre_completo
        except Exception:
            _actividad.npo_ingeniero = None
        try:
            _actividad.npo_estado_asignacion = self.estado_asignacion
        except Exception:
            _actividad.npo_estado_asignacion = None
        try:
            _actividad.npo_concepto = self.npo_concepto
        except Exception:
            _actividad.npo_concepto = None
        try:
            _actividad.npo_tipo_intervencion = self.tipo_intervencion
        except Exception:
            _actividad.npo_tipo_intervencion = None
        try:
            _actividad.npo_fecha_asignacion = self.fecha_asignacion
        except Exception:
            _actividad.npo_fecha_asignacion = None
        try:
            _actividad.npo_fm_supervisor = self.fm_supervisor.nombre_completo
        except Exception:
            _actividad.npo_fm_supervisor = None
        try:
            _actividad.estado_ultimo = self.estado_asignacion
            if _actividad.estado_noc == PRODUCCION:
                _actividad.estado_ultimo = PRODUCCION
        except Exception:
            _actividad.estado_ultimo = None

        try:
            if _actividad.npo_estado_asignacion == _actividad.ni_estado_asignacion:
                _actividad.estado_unico = _actividad.npo_estado_asignacion

            if _actividad.npo_estado_asignacion == ASIGNADA or _actividad.ni_estado_asignacion == ASIGNADA:
                _actividad.estado_unico = ASIGNADA

            # if _actividad.npo_estado_asignacion == None and _actividad.ni_estado_asignacion != None:
            #     _actividad.estado_unico = __actividad.ni_estado_asignacion
            #
            # if _actividad.ni_estado_asignacion == None and _actividad.npo_estado_asignacion != None:
            #     _actividad.estado_unico = __actividad.npo_estado_asignacion

            if _actividad.npo_estado_asignacion != None and _actividad.ni_estado_asignacion == None:
                _actividad.estado_unico = _actividad.npo_estado_asignacion

            if _actividad.ni_estado_asignacion != None and _actividad.npo_estado_asignacion == None:
                _actividad.estado_unico = _actividad.ni_estado_asignacion

            if _actividad.npo_estado_asignacion == REQUIERE_VISITA and _actividad.ni_estado_asignacion != ASIGNADA:
                _actividad.estado_unico = REQUIERE_VISITA

            if _actividad.ni_estado_asignacion == REQUIERE_VISITA and _actividad.npo_estado_asignacion != ASIGNADA:
                _actividad.estado_unico = REQUIERE_VISITA

            if _actividad.npo_estado_asignacion == EN_MONITOREO and _actividad.ni_estado_asignacion != ASIGNADA and _actividad.ni_estado_asignacion != REQUIERE_VISITA:
                _actividad.estado_unico = EN_MONITOREO

            if _actividad.ni_estado_asignacion == EN_MONITOREO and _actividad.npo_estado_asignacion != ASIGNADA and _actividad.npo_estado_asignacion != REQUIERE_VISITA:
                _actividad.estado_unico = EN_MONITOREO

            if _actividad.npo_estado_asignacion == ENVIADO_A_SEGUIMIENTO and _actividad.ni_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ENVIADO_A_SEGUIMIENTO

            if _actividad.ni_estado_asignacion == ENVIADO_A_SEGUIMIENTO and _actividad.npo_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ENVIADO_A_SEGUIMIENTO

            if _actividad.npo_estado_asignacion == ESCALADO_A_CLARO and _actividad.ni_estado_asignacion == ENVIADO_A_SEGUIMIENTO:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.npo_estado_asignacion == ESCALADO_A_CLARO and _actividad.ni_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.ni_estado_asignacion == ESCALADO_A_CLARO and _actividad.npo_estado_asignacion == ENVIADO_A_SEGUIMIENTO:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.ni_estado_asignacion == ESCALADO_A_CLARO and _actividad.npo_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.estado_noc == PRODUCCION:
                _actividad.estado_unico = PRODUCCION
        except Exception:
            _actividad.estado_unico = None

        _actividad.save()

        super(AsignacionNpo, self).save(*args, **kwargs)


class AsignacionNi(models.Model):
    ni_asignador = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_ni_asignador')
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_ni_ingeniero')
    ni_ingeniero_celular = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero_empresa = models.CharField(max_length=255, blank=True, null=True)
    fm_supervisor = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_ni_fm_supervisor')
    fm_supervisor_celular = models.CharField(max_length=255, blank=True, null=True)
    fm_supervisor_empresa = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_ni')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='asignaciones_ni')
    wp = models.BigIntegerField(blank=True, null=True)
    estado_asignacion = models.CharField(max_length=255, choices=choices.ESTADO_ASIGNACION_CHOICES, default='Asignada', blank=True, null=True)
    origen_falla = models.CharField(max_length=255, choices=choices.ORIGEN_FALLA_CHOICES, blank=True, null=True)
    tipo_intervencion = models.CharField(max_length=255, choices=choices.TIPO_INTERVENCION_CHOICES, blank=True, null=True)
    fecha_asignacion = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    # Extra fields

    # conceptos ni
    ni_concepto = models.TextField(blank=True, null=True, editable=False)
    ni_estado_solicitud_hw = models.CharField(max_length=255, blank=True, null=True, editable=False)

    class Meta:
        ordering = ('creado',)
        verbose_name = "asignacion ni"
        verbose_name_plural = "asignaciones ni"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('asignaciones:detail_asignacion_ni', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        _actividad = Actividad.objects.get(id=self.actividad.id)

        # asignaciones ni
        try:
            _actividad.ni_ingeniero = self.ni_ingeniero.nombre_completo
        except Exception:
            _actividad.ni_ingeniero = None
        try:
            _actividad.ni_estado_asignacion = self.estado_asignacion
        except Exception:
            _actividad.ni_estado_asignacion = None
        try:
            _actividad.ni_origen_falla = self.origen_falla
        except Exception:
            _actividad.ni_origen_falla = None
        try:
            _actividad.ni_concepto = self.ni_concepto
        except Exception:
            _actividad.ni_concepto = None
        try:
            _actividad.ni_estado_solicitud_hw = self.ni_estado_solicitud_hw
        except Exception:
            _actividad.ni_estado_solicitud_hw = None
        try:
            _actividad.ni_tipo_intervencion = self.tipo_intervencion
        except Exception:
            _actividad.ni_tipo_intervencion = None
        try:
            _actividad.ni_fecha_asignacion = self.fecha_asignacion
        except Exception:
            _actividad.ni_fecha_asignacion = None
        try:
            _actividad.ni_fm_supervisor = self.fm_supervisor.nombre_completo
        except Exception:
            _actividad.ni_fm_supervisor = None
        try:
            _actividad.estado_ultimo = self.estado_asignacion
            if _actividad.estado_noc == PRODUCCION:
                _actividad.estado_ultimo = PRODUCCION
        except Exception:
            _actividad.estado_ultimo = None

        try:
            if _actividad.npo_estado_asignacion == _actividad.ni_estado_asignacion:
                _actividad.estado_unico = _actividad.npo_estado_asignacion

            if _actividad.npo_estado_asignacion == ASIGNADA or _actividad.ni_estado_asignacion == ASIGNADA:
                _actividad.estado_unico = ASIGNADA

            # if _actividad.npo_estado_asignacion == None and _actividad.ni_estado_asignacion != None:
            #     _actividad.estado_unico = __actividad.ni_estado_asignacion
            #
            # if _actividad.ni_estado_asignacion == None and _actividad.npo_estado_asignacion != None:
            #     _actividad.estado_unico = __actividad.npo_estado_asignacion

            if _actividad.npo_estado_asignacion != None and _actividad.ni_estado_asignacion == None:
                _actividad.estado_unico = _actividad.npo_estado_asignacion

            if _actividad.ni_estado_asignacion != None and _actividad.npo_estado_asignacion == None:
                _actividad.estado_unico = _actividad.ni_estado_asignacion

            if _actividad.npo_estado_asignacion == REQUIERE_VISITA and _actividad.ni_estado_asignacion != ASIGNADA:
                _actividad.estado_unico = REQUIERE_VISITA

            if _actividad.ni_estado_asignacion == REQUIERE_VISITA and _actividad.npo_estado_asignacion != ASIGNADA:
                _actividad.estado_unico = REQUIERE_VISITA

            if _actividad.npo_estado_asignacion == EN_MONITOREO and _actividad.ni_estado_asignacion != ASIGNADA and _actividad.ni_estado_asignacion != REQUIERE_VISITA:
                _actividad.estado_unico = EN_MONITOREO

            if _actividad.ni_estado_asignacion == EN_MONITOREO and _actividad.npo_estado_asignacion != ASIGNADA and _actividad.npo_estado_asignacion != REQUIERE_VISITA:
                _actividad.estado_unico = EN_MONITOREO

            if _actividad.npo_estado_asignacion == ENVIADO_A_SEGUIMIENTO and _actividad.ni_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ENVIADO_A_SEGUIMIENTO

            if _actividad.ni_estado_asignacion == ENVIADO_A_SEGUIMIENTO and _actividad.npo_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ENVIADO_A_SEGUIMIENTO

            if _actividad.npo_estado_asignacion == ESCALADO_A_CLARO and _actividad.ni_estado_asignacion == ENVIADO_A_SEGUIMIENTO:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.npo_estado_asignacion == ESCALADO_A_CLARO and _actividad.ni_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.ni_estado_asignacion == ESCALADO_A_CLARO and _actividad.npo_estado_asignacion == ENVIADO_A_SEGUIMIENTO:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.ni_estado_asignacion == ESCALADO_A_CLARO and _actividad.npo_estado_asignacion == NO_EXITOSA:
                _actividad.estado_unico = ESCALADO_A_CLARO

            if _actividad.estado_noc == PRODUCCION:
                _actividad.estado_unico = PRODUCCION
        except Exception:
            _actividad.estado_unico = None

        _actividad.save()

        super(AsignacionNi, self).save(*args, **kwargs)
