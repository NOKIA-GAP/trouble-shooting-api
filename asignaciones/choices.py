# -*- coding: utf-8 -*-

""" ESTADO_ASIGNACION_CHOICES  """
ESTADO_ASIGNACION_CHOICES = (
    ('', '---------'),
    ('Asignada', 'Asignada'),
    ('En monitoreo', 'En monitoreo'),
    ('Enviado a seguimiento', 'Enviado a seguimiento'),
    ('Requiere visita', 'Requiere visita'),
    ('No exitosa', 'No exitosa'),
    ('Escalado a claro', 'Escalado a claro'),
)

""" POSIBLE_CAUSA_CHOICES  """
POSIBLE_CAUSA_CHOICES = (
    ('', '---------'),
    ('Instalacion', 'Instalacion'),
    ('Software', 'Software'),
    ('Hardware', 'Hardware'),
    ('Datafill', 'Datafill'),
    ('Ajuste Potencia', 'Ajuste Potencia'),
    ('Integracion', 'Integracion'),
    ('Interferencia externa', 'Interferencia externa'),
    ('Cambio diseno', 'Cambio diseno'),
    ('Mal rechazo', 'Mal rechazo'),
    ('Otra causa', 'Otra causa'),
)

""" TIPO_INTERVENCION_CHOICES  """
TIPO_INTERVENCION_CHOICES = (
    ('', '---------'),
    ('Local', 'Local'),
    ('Remoto', 'Remoto'),
)
