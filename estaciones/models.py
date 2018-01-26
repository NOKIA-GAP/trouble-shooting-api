# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from . import choices

class Estacion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    regional = models.CharField(max_length=255, choices=choices.REGIONAL_CHOICES)
    ciudad = models.CharField(max_length=255, choices=choices.CIUDAD_CHOICES)
    responsable = models.CharField(max_length=255, choices=choices.RESPONSABLE_CHOICES, blank=True, null=True)
    prioridad = models.CharField(max_length=255, choices=choices.PRIORIDAD_CHOICES, blank=True, null=True)
    estado_estacion = models.CharField(max_length=255, blank=True, null=True, editable=False)
    numero_actividades = models.PositiveIntegerField(blank=True, null=True, editable=False)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "estacion"
        verbose_name_plural = "estaciones"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})
