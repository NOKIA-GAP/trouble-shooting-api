# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from estaciones.models import Estacion
from actividades.models import Actividad
from asignaciones.models import AsignacionNpo, AsignacionNi
from django.contrib.auth.models import User
from users.models import Perfil

class ConceptoNpo(models.Model):
    npo_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_npo')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_npo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_npo')
    asignacion_npo = models.ForeignKey(AsignacionNpo, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_npo')
    wp = models.BigIntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='concepto_npo/imagen', blank=True, null=True)
    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "concepto npo"
        verbose_name_plural = "conceptos npo"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('conceptos:detail_concepto_npo', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # actividad
        _actividad = Actividad.objects.get(id=self.actividad.id)
        # asignacion npo
        try:
            _asignacion = AsignacionNpo.objects.get(id=self.asignacion_npo.id)
        except Exception:
            pass
        # conceptos npo

        # actividad
        try:
            _actividad.npo_concepto = self.contenido
        except Exception:
            _actividad.npo_concepto = None
        # asignacion npo
        try:
            _asignacion.npo_concepto = self.contenido
        except Exception:
            try:
                _asignacion.npo_concepto = None
            except Exception:
                pass

        _actividad.save()
        try:
            _asignacion.save()
        except Exception:
            pass

        super(ConceptoNpo, self).save(*args, **kwargs)

class ConceptoNi(models.Model):
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_ni')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_ni')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_ni')
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='conceptos_ni')
    wp = models.BigIntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='concepto_ni/imagen', blank=True, null=True)
    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "concepto ni"
        verbose_name_plural = "conceptos ni"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('conceptos:detail_concepto_ni', kwargs={'pk': self.pk})

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
            _actividad.ni_concepto = self.contenido
        except Exception:
            _actividad.ni_concepto = None
        # asignacion ni
        try:
            _asignacion.ni_concepto = self.contenido
        except Exception:
            try:
                _asignacion.ni_concepto = None
            except Exception:
                pass

        _actividad.save()
        try:
            _asignacion.save()
        except Exception:
            pass

        super(ConceptoNi, self).save(*args, **kwargs)
