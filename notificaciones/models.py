from django.db import models
from asignaciones.models import AsignacionNi
from actividades.models import Actividad
from estaciones.models import Estacion
from users.models import Perfil
from . import choices

class NotificacionRequiereVisita(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_requiere_visita')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
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
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
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
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
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

class NotificacionFallaSoftware(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_software')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_software')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_software')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_software')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla software"
        verbose_name_plural = "notificaciones falla software"

    def __str__(self):
        return str(self.id)

class NotificacionFallaHardware(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_hardware')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_hardware')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_hardware')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_hardware')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla hardware"
        verbose_name_plural = "notificaciones falla hardware"

    def __str__(self):
        return str(self.id)

class NotificacionFallaDatafill(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_datafill')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_datafill')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_datafill')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_datafill')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla datafill"
        verbose_name_plural = "notificaciones falla datafill"

    def __str__(self):
        return str(self.id)

class NotificacionFallaAjustePotencia(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_ajuste_potencia')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_ajuste_potencia')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_ajuste_potencia')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_ajuste_potencia')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla ajuste potencia"
        verbose_name_plural = "notificaciones falla ajuste potencia"

    def __str__(self):
        return str(self.id)

class NotificacionFallaInterferenciaExterna(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_interferencia_externa')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_interferencia_externa')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_interferencia_externa')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_interferencia_externa')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla interferencia externa"
        verbose_name_plural = "notificaciones falla interferencia externa"

    def __str__(self):
        return str(self.id)

class NotificacionFallaCambioDiseno(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_cambio_diseno')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_cambio_diseno')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_cambio_diseno')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_cambio_diseno')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla cambio diseno"
        verbose_name_plural = "notificaciones falla cambio diseno"

    def __str__(self):
        return str(self.id)

class NotificacionFallaMalRechazo(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_mal_rechazo')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
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

class NotificacionFallaTX(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_tx')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_tx')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_tx')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_tx')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla TX"
        verbose_name_plural = "notificaciones falla TX"

    def __str__(self):
        return str(self.id)

class NotificacionFallaComportamientoEsperado(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_esperado')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_esperado')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_esperado')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_esperado')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla comportamiento esperado"
        verbose_name_plural = "notificaciones falla comportamiento esperado"

    def __str__(self):
        return str(self.id)

class NotificacionFallaComportamientoPrevio(models.Model):
    asignacion_ni = models.ForeignKey(AsignacionNi, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_previo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_previo')
    wp = models.BigIntegerField(blank=True, null=True)
    service_supplier = models.CharField(max_length=255, choices=choices.SERVICE_SUPPLIER_CHOICES, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_previo')
    banda = models.CharField(max_length=255, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    ni_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='notificaciones_falla_comportamiento_previo')
    concepto = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "notificacion falla comportamiento previo"
        verbose_name_plural = "notificaciones falla comportamiento previo"

    def __str__(self):
        return str(self.id)
