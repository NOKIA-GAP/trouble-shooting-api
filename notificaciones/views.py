from django.shortcuts import render
from django.http import HttpResponse
from .models import (
NotificacionRequiereVisita,
NotificacionFallaInstalacion,
NotificacionFallaIntegracion,
)
from .resources import (
NotificacionRequiereVisitaResource,
NotificacionFallaInstalacionResource,
NotificacionFallaIntegracionResource,
)

def export_notificaciones_requiere_visita(request):
    notificaciones_requiere_visita = NotificacionRequiereVisitaResource()
    dataset = notificaciones_requiere_visita.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionRequiereVisita.xlsx"'
    return response

def export_notificaciones_falla_instalacion(request):
    notificaciones_falla_instalacion = NotificacionFallaInstalacionResource()
    dataset = notificaciones_falla_instalacion.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaInstalacion.xlsx"'
    return response

def export_notificaciones_falla_integracion(request):
    notificaciones_falla_integracion = NotificacionFallaIntegracionResource()
    dataset = notificaciones_falla_integracion.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="NotificacionFallaIntegracion.xlsx"'
    return response
