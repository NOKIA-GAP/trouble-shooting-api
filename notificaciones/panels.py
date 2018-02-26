from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
)

notificaciones_requiere_visita = NotificacionRequiereVisita.objects.all()
notificaciones_falla_instalacion = NotificacionFallaInstalacion.objects.all()
notificaciones_falla_integracion = NotificacionFallaIntegracion.objects.all()
