from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
NotificacionFallaSoftware,
NotificacionFallaHardware,
NotificacionFallaDatafill,
NotificacionFallaAjustePotencia,
NotificacionFallaInterferenciaExterna,
NotificacionFallaCambioDiseno,
NotificacionFallaMalRechazo,
NotificacionFallaTX,
NotificacionFallaComportamientoEsperado,
NotificacionFallaComportamientoPrevio,
)

notificaciones_requiere_visita = NotificacionRequiereVisita.objects.all()
notificacion_falla_instalacion = NotificacionFallaInstalacion.objects.all()
notificacion_falla_integracion = NotificacionFallaIntegracion.objects.all()
notificacion_falla_software = NotificacionFallaSoftware.objects.all()
notificacion_falla_hardware = NotificacionFallaHardware.objects.all()
notificacion_falla_datafill = NotificacionFallaDatafill.objects.all()
notificacion_falla_ajuste_potencia = NotificacionFallaAjustePotencia.objects.all()
notificacion_falla_interferencia_externa = NotificacionFallaInterferenciaExterna.objects.all()
notificacion_falla_cambio_diseno = NotificacionFallaCambioDiseno.objects.all()
notificacion_falla_mal_rechazo = NotificacionFallaMalRechazo.objects.all()
notificacion_falla_tx = NotificacionFallaTX.objects.all()
notificacion_falla_comportamiento_esperado = NotificacionFallaComportamientoEsperado.objects.all()
notificacion_falla_comportamiento_previo = NotificacionFallaComportamientoPrevio.objects.all()
