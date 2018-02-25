from django.db import models
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil
from . import choices

class Falla(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='fallas')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='fallas')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='fallas')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='fallas')
    concepto = models.TextField(blank=True, null=True)
    tipo_falla = models.CharField(max_length=255, choices=choices.TIPO_FALLA_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "falla"
        verbose_name_plural = "fallas"

    def __str__(self):
        return str(self.id)
