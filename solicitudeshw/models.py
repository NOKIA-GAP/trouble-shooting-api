# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from users.models import Perfil
from asignaciones.models import AsignacionNi
from estaciones.models import Estacion
from actividades.models import Actividad
from . import choices
from django.core.validators import MinValueValidator

class SolicitudHW(models.Model):
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitudeshw')
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitudeshw')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitudeshw')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitudeshw')
    wp = models.BigIntegerField(blank=True, null=True)

    estado_solicitud = models.CharField(max_length=255, choices=choices.ESTADO_SOLICITUD_CHOICES, default='Requiere HW', blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "solicitudhw"
        verbose_name_plural = "solicitudeshw"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('solicitudeshw:detail_solicitudhw', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # actividad
        _actividad = Actividad.objects.get(id=self.actividad.id)
        # asignacion ni
        try:
            _asignacion = AsignacionNi.objects.get(id=self.asignacion_ni.id)
        except Exception:
            pass
        # conceptos ni

        # actividad
        try:
            _actividad.ni_estado_solicitud_hw = self.estado_solicitud
        except Exception:
            _actividad.ni_estado_solicitud_hw = None
        # asignacion ni
        try:
            _asignacion.ni_estado_solicitud_hw = self.estado_solicitud
        except Exception:
            try:
                _asignacion.ni_estado_solicitud_hw = None
            except Exception:
                pass

        _actividad.save()
        try:
            _asignacion.save()
        except Exception:
            pass

        super(SolicitudHW, self).save(*args, **kwargs)

class Solicitud(models.Model):
    solicitudhw = models.ForeignKey(SolicitudHW, on_delete=models.CASCADE, blank=True, null=True, related_name='solicitudes')
    hardware = models.CharField(max_length=255, choices=choices.HARDWARE_CHOICES, blank=True, null=True)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('solicitudeshw:detail_solicitud', kwargs={'pk': self.pk})
