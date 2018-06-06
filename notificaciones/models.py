from django.db import models
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil
from . import choices
from actividades import choices as actividades_choices

class NotificacionRequiereVisita(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=actividades_choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    detalle_solicitud_visita = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion requiere visita"
        verbose_name_plural = "notificaciones requiere visita"

    def __str__(self):
        return str(self.id)

class NotificacionFallaInstalacion(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_instalacion')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_instalacion')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=actividades_choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_instalacion')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_instalacion')
    detalle_falla_instalacion = models.TextField(blank=True, null=True)
    solver = models.CharField(max_length=255, choices=choices.SOLVER_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla instalacion"
        verbose_name_plural = "notificaciones falla instalacion"

    def __str__(self):
        return str(self.id)

class NotificacionFallaIntegracion(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_integracion')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_integracion')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=actividades_choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_integracion')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_integracion')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla integracion"
        verbose_name_plural = "notificaciones falla integracion"

    def __str__(self):
        return str(self.id)

class NotificacionFallaMalRechazo(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=actividades_choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla mal rechazo"
        verbose_name_plural = "notificaciones falla mal rechazo"

    def __str__(self):
        return str(self.id)
