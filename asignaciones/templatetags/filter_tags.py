from django import template
from asignaciones.models import AsignacionNpo, AsignacionNi

register = template.Library()

@register.filter
def estado_asignacion_npo(asignaciones_npo_ingeniero, estado):
    qs_npo = asignaciones_npo_ingeniero.filter(estado_asignacion=estado).count()
    return qs_npo

@register.filter
def estado_asignacion_ni(asignaciones_ni_ingeniero, estado):
    qs_ni = asignaciones_ni_ingeniero.filter(estado_asignacion=estado).count()
    return qs_ni
