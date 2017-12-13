# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib

from django import template

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
