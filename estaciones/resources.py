# -*- coding: utf-8 -*-s
from import_export import resources
from .models import Estacion

class EstacionResource(resources.ModelResource):

    class Meta:
        model = Estacion
        exclude = ( 'creado', 'actualizado', )
