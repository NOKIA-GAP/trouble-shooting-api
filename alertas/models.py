from django.db import models

from estaciones.models import Estacion
from actividades.models import Actividad
from . import choices

class Alerta(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='alertas')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='alertas')
    wp = models.BigIntegerField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    estado_alerta = models.CharField(max_length=255, choices=choices.ESTADO_ALERTA_CHOICES, default='Abierto', blank=True, null=True)
    tipo_alerta = models.CharField(max_length=255, choices=choices.TIPO_ALERTA_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "alerta"
        verbose_name_plural = "alertas"

    def __str__(self):
        return str(self.id)
