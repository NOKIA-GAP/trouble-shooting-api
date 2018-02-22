# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib

from django import template
from asignaciones.models import AsignacionNpo, AsignacionNi

register = template.Library()

def replace_underscore(value, arg):
    return value.replace(arg, ' ')

register.filter('replace_underscore', replace_underscore)

@register.filter
def get_encoded_dict(query_dict):
    return urllib.parse.urlencode(query_dict)

@register.simple_tag
def relative_url(value, field, urlencode=None):
    url = '?{}={}'.format(field, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url

@register.filter
def estado_asignacion_npo(value, args):
    args = args.split(',')
    qs = value.filter(estado_asignacion=args[0], tipo_intervencion=args[1]).count()
    return qs

@register.filter
def estado_asignacion_npo_estacion(value, args):
    args = args.split(',')
    qs = value.filter(estado_asignacion=args[0], tipo_intervencion=args[1]).values_list('estacion', flat=True).distinct().count()
    return qs

@register.filter
def estado_asignacion_ni(value, args):
    args = args.split(',')
    qs = value.filter(estado_asignacion=args[0], tipo_intervencion=args[1]).count()
    return qs

@register.filter
def estado_asignacion_ni_estacion(value, args):
    args = args.split(',')
    qs = value.filter(estado_asignacion=args[0], tipo_intervencion=args[1]).values_list('estacion', flat=True).distinct().count()
    return qs

@register.filter
def estado_incidente_npo(incidentes_npo, estado):
    qs = incidentes_npo.filter(estado_incidente=estado).count()
    return qs

@register.filter
def estado_incidente_ni(incidentes_ni, estado):
    qs = incidentes_ni.filter(estado_incidente=estado).count()
    return qs
