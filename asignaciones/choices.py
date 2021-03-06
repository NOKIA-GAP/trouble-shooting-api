# -*- coding: utf-8 -*-

""" ESTADO_ASIGNACION_CHOICES  """
ESTADO_ASIGNACION_CHOICES = (
    ('', '---------'),
    ('Asignada', 'Asignada'),
    ('En monitoreo', 'En monitoreo'),
    ('Enviado a seguimiento', 'Enviado a seguimiento'),
    ('Requiere visita', 'Requiere visita'),
    # ('No exitosa', 'No exitosa'),
    ('Escalado a claro', 'Escalado a claro'),
    ('Requiere segunda revision', 'Requiere segunda revision'),
)

""" ORIGEN_FALLA_CHOICES  """
ORIGEN_FALLA_CHOICES = (
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
    ('TX', 'TX'),
    ('Falla Externa', 'Falla Externa'),
    ('Falla TSS', 'Falla TSS'),
    ('Ajuste Adyacencias', 'Ajuste Adyacencias'),
)

""" SOLVER_CHOICES  """
SOLVER_CHOICES = (
    ('', '---------'),
    ('Nokia', 'Nokia'),
    ('Service suplier', 'Service suplier'),
)

""" TIPO_INTERVENCION_CHOICES  """
TIPO_INTERVENCION_CHOICES = (
    ('', '---------'),
    ('Local', 'Local'),
    ('Remoto', 'Remoto'),
)

""" HARDWARE_PROPIETARIO_CHOICES  """
HARDWARE_PROPIETARIO_CHOICES = (
    ('', '---------'),
    ('NOKIA', 'NOKIA'),
    ('CLARO', 'CLARO'),
    ('TERCEROS', 'TERCEROS'),
)

""" CLASIFICACION_PREVIA_CHOICES  """
CLASIFICACION_PREVIA_CHOICES = (
    ('', '---------'),
    ('Instalacion', 'Instalacion'),
    ('Quality', 'Quality'),
    ('Perdida de Trafico', 'Perdida de Trafico'),
    ('Denied/Drop', 'Denied/Drop'),
    ('Software', 'Software'),
    ('Handover', 'Handover'),
    ('Configuracion', 'Configuracion'),
    ('Mal Rechazo', 'Mal Rechazo'),
)
