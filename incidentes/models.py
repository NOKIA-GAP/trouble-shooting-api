from django.db import models
from django.urls import reverse
from estaciones.models import Estacion
from actividades.models import Actividad
from users.models import Perfil
from . import choices

class IncidenteNpo(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_npo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_npo')
    wp = models.BigIntegerField(blank=True, null=True)
    npo_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_npo')
    estado_incidente = models.CharField(max_length=255, choices=choices.ESTADO_INCIDENTE_CHOICES, default='Abierto', blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'incidente npo'
        verbose_name_plural = 'incidentes npo'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('incidentes:detail_incidente_npo', kwargs={'pk': self.pk})

class IncidenteNi(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_ni')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_ni')
    wp = models.BigIntegerField(blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='incidentes_ni')
    estado_incidente = models.CharField(max_length=255, choices=choices.ESTADO_INCIDENTE_CHOICES, default='Abierto', blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'incidente ni'
        verbose_name_plural = 'incidentes ni'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('incidentes:detail_incidente_ni', kwargs={'pk': self.pk})
