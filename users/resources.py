# -*- coding: utf-8 -*-s
from import_export import resources
from .models import Perfil

class PerfilResource(resources.ModelResource):

    class Meta:
        model = Perfil
        # exclude = (, )
        export_order = (
        'id',
        'user',
        'slug',
        'perfil_usuario',
        'nombre',
        'apellido',
        'nombre_completo',
        'email',
        'celular',
        'creado',
        'actualizado',
        )
