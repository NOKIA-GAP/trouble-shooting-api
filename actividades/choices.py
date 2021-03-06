# -*- coding: utf-8 -*-

""" TIPO_TRABAJO_CHOICES  """
TIPO_TRABAJO_CHOICES = (
    ('LTE Overlay', 'LTE Overlay'),
    ('Tercera Portadora', 'Tercera Portadora'),
    ('3G Huawei Overlay', '3G Huawei Overlay'),
    ('Sitio Nuevo 3G', 'Sitio Nuevo 3G'),
    ('Sitio Nuevo 2G PE', 'Sitio Nuevo 2G PE'),
    ('Sitio Nuevo LTE', 'Sitio Nuevo LTE'),
    ('Sector Expansion', 'Sector Expansion'),
    ('Sitio Nuevo 3G PE', 'Sitio Nuevo 3G PE'),
    ('3G Overlay', '3G Overlay'),
    ('Cambio de Jumpers y Breaker_CP', 'Cambio de Jumpers y Breaker_CP'),
    ('Cambio HW para MC_CP', 'Cambio HW para MC_CP'),
    ('Channel Element_CP', 'Channel Element_CP'),
    ('Adecuaciones LTE', 'Adecuaciones LTE'),
    ('Cuarta Portadora', 'Cuarta Portadora'),
    ('Cambio HW para MC', 'Cambio HW para MC'),
    ('Modernizacion Multiradio', 'Modernizacion Multiradio'),
    ('Channel Element_MMR', 'Channel Element_MMR'),
    ('Segundo Nodo', 'Segundo Nodo'),
    ('Channel Element_5P', 'Channel Element_5P'),
    ('Reubicacion', 'Reubicacion'),
    ('Sitio Nuevo LTE PE', 'Sitio Nuevo LTE PE'),
    ('Sector Expansion Huawei', 'Sector Expansion Huawei'),
    ('Cambio de Jumpers y RRU', 'Cambio de Jumpers y RRU'),
    ('Cambio HW para MC Huawei', 'Cambio HW para MC Huawei'),
    ('Swap', 'Swap'),
    ('Cambio HW LTE', 'Cambio HW LTE'),
    ('Sitio Nuevo 3G/LTE Temporal', 'Sitio Nuevo 3G/LTE Temporal'),
    ('Cambio de Jumpers y Breaker', 'Cambio de Jumpers y Breaker'),
    ('Cambio de Jumpers y Breaker_5P', 'Cambio de Jumpers y Breaker_5P'),
    ('Adecuaciones SE', 'Adecuaciones SE'),
    ('LTE Huawei Overlay', 'LTE Huawei Overlay'),
    ('Adecuaciones LTE Huawei', 'Adecuaciones LTE Huawei'),
    ('Channel Element', 'Channel Element'),
    ('Cambio HW para MC_5P', 'Cambio HW para MC_5P'),
    ('Cambio HW para MC_5P y RF', 'Cambio HW para MC_5P y RF'),
    ('Swap Antenas Capa 4-5', 'Swap Antenas Capa 4-5'),
    ('Channel Element + Upgrade Modulos RF', 'Channel Element + Upgrade Modulos RF'),
    ('Channel Element_5P y RF', 'Channel Element_5P y RF'),
    ('Cuarta Portadora Huawei', 'Cuarta Portadora Huawei'),
    ('Tercera Portadora Huawei', 'Tercera Portadora Huawei'),
    ('Adecuaciones Overlay', 'Adecuaciones Overlay'),
    ('Adecuacion para LTE 1900Mhz', 'Adecuacion para LTE 1900Mhz'),
    ('Upgrade Modulos RF', 'Upgrade Modulos RF'),
    ('Cambio Feeder a Fibra', 'Cambio Feeder a Fibra'),
    ('RF Sharing a Dedicado', 'RF Sharing a Dedicado'),
    ('Reubicacion Equipos', 'Reubicacion Equipos'),
    ('Cambio HW', 'Cambio HW'),
    ('Modernizacion Concurrente', 'Modernizacion Concurrente'),
    ('Cambio de Jumpers', 'Cambio de Jumpers'),
    ('2G Overlay', '2G Overlay'),
)

""" ESTADO_NOC_CHOICES  """
ESTADO_NOC_CHOICES = (
    ('Produccion', 'Produccion'),
    ('Escalado a Implementacion', 'Escalado a Implementacion'),
    ('Escalado a Grupo Calidad', 'Escalado a Grupo Calidad'),
    ('Escalado a RF', 'Escalado a RF'),
    ('Escalado a OyM', 'Escalado a OyM'),
    ('Escalado a GDRT', 'Escalado a GDRT'),
    ('Escalado Control Cambios', 'Escalado Control Cambios'),
    ('Seguimiento 12h', 'Seguimiento 12h'),
    ('Seguimiento 24h', 'Seguimiento 24h'),
    ('Seguimiento 36h', 'Seguimiento 36h'),
    ('PreCheck', 'PreCheckC'),
    ('Pendiente Remedy', 'Pendiente Remedy'),
    ('Stand By', 'Stand By'),
    ('Rollback', 'Rollback'),
    ('Suspendido', 'Suspendido'),
)



""" SUBESTADO_NOC_CHOICES  """
SUBESTADO_NOC_CHOICES = (
    ('Alarmas', 'Alarmas'),
    ('Alarmas de HW', 'Alarmas de HW'),
    ('Alarmas de Rx Sistema Radiante', 'Alarmas de Rx Sistema Radiante'),
    ('Alarmas de TX', 'Alarmas de TX'),
    ('Alarmas de energia', 'Alarmas de energia'),
    ('Alarmas TRAFFIC CHAN', 'Alarmas TRAFFIC CHAN'),
    ('Alto RTWP', 'Alto RTWP'),
    ('Causa Externa', 'Causa Externa'),
    ('Degradacion KPI', 'Degradacion KPI'),
    ('Error Comisionamiento BTS', 'Error Comisionamiento BTS'),
    ('Error Configuracion Acceso', 'Error Configuracion Acceso'),
    ('Error de Instalacion', 'Error de Instalacion'),
    ('Error comisionamiento BTS', 'Error comisionamiento BTS'),
    ('Error configuracion Acceso', 'Error configuracion Acceso'),
    ('Error de instalacion', 'Error de instalacion'),
    ('Fuera de servicio', 'Fuera de servicio'),
    ('Produccion', 'Produccion'),
    ('Pendiente CRQ', 'Pendiente CRQ'),
    ('Pendiente DF', 'Pendiente DF'),
    ('Pendiente Evidencias', 'Pendiente Evidencias'),
    ('Pendiente Pruebas Alarmas', 'Pendiente Pruebas Alarmas'),
    ('Pendiente Sitio Limpio', 'Pendiente Sitio Limpio'),
    ('Pendiente Tareas Remedy', 'Pendiente Tareas Remedy'),
    ('Pendiente Testgestion', 'Pendiente Testgestion'),
    ('Pendiente Remedy', 'Pendiente Remedy'),
    ('Pendiente Actualizacion DF', 'Pendiente Actualizacion DF'),
    ('Pendiente Notificacion', 'Pendiente Notificacion'),
    ('Perdida de Paquetes', 'Perdida de Paquetes'),
    ('Produccion', 'Produccion'),
    ('Revision Parcial', 'Revision Parcial'),
    ('Reinicio 12Hrs', 'Reinicio 12Hrs'),
    ('Seguimiento 12H', 'Seguimiento 12H'),
    ('Seguimiento 24H', 'Seguimiento 24H'),
    ('Seguimiento 36H', 'Seguimiento 36H'),
    ('Precheck', 'Precheck'),
    ('Sin Trafico', 'Sin Trafico'),
    ('Sitio Fuera de Servicio', 'Sitio Fuera de Servicio'),
    ('Sin Conexion Remota', 'Sin Conexion Remota'),
    ('Stand By', 'Stand By'),
    ('Adyacencias Faltantes', 'Adyacencias Faltantes'),
)

""" VISITA_SUPERVISOR_CHOICES  """
VISITA_SUPERVISOR_CHOICES = (
    ('Fabian Barbosa', 'Fabian Barbosa'),
    ('Andres Cardenas', 'Andres Cardenas'),
    ('Jonathan Cuervo', 'Jonathan Cuervo'),
    ('Carlos Santos', 'Carlos Santos'),
    ('Jimmy Sepulveda', 'Jimmy Sepulveda'),
    ('Wilson Bohorquez', 'Wilson Bohorquez'),
    ('Mario Fiallo', 'Mario Fiallo'),
    ('Hober Sanchez', 'Hober Sanchez'),
    ('Leonardo Alarcon', 'Leonardo Alarcon'),
    ('Ruben Alvarado', 'Ruben Alvarado'),
    ('Diego Medina', 'Diego Medina'),
    ('Jhon Uparela', 'Jhon Uparela'),
    ('Carlos Funeme', 'Carlos Funeme'),
    ('Yony Sanchez', 'Yony Sanchez'),
    ('Ramon montagut', 'Ramon montagut'),
    ('Richard Luna', 'Richard Luna'),
    ('Jolman Castillo', 'Jolman Castillo'),
    ('Manuel Garcia', 'Manuel Garcia'),
)

""" IMPACTO_DEGRADACION_CHOICES  """
IMPACTO_DEGRADACION_CHOICES = (
    ('Leve', 'Leve'),
    ('Grave', 'Grave'),
)

""" GRUPO_GAP_CHOICES  """
GRUPO_GAP_CHOICES = (
    ('GAP1', 'GAP1'),
    ('GAP2', 'GAP2'),
    ('ZTE', 'ZTE'),
)

""" SERVICE_SUPPLIER_CHOICES  """
SERVICE_SUPPLIER_CHOICES = (
    ('DECOM', 'DECOM'),
    ('INGETEL', 'INGETEL'),
    ('ENECON', 'ENECON'),
    ('NEXPRO', 'NEXPRO'),
    ('JANACOR', 'JANACOR'),
    ('UNION', 'UNION'),
    ('OPTIMACOM', 'OPTIMACOM'),
    ('DELTEC', 'DELTEC'),
    ('FIBRATERRA', 'FIBRATERRA'),
    ('ADSM', 'ADSM'),
    ('SERVINTELCO', 'SERVINTELCO'),
    ('EZENTIS', 'EZENTIS'),
    ('SITCOM', 'SITCOM'),
    ('INGYTELCOM', 'INGYTELCOM'),
    ('SAI', 'SAI'),
    ('GAMMA', 'GAMMA'),
    ('PACIFIC ENERGY', 'PACIFIC ENERGY'),
    ('NEOSTAR', 'NEOSTAR'),
    ('DASCON', 'DASCON'),
    ('ATENA', 'ATENA'),
    ('ZOOM', 'ZOOM'),
    ('LINEA', 'LINEA'),
    ('WISECA', 'WISECA'),
    ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'),
    ('NESITELCO', 'NESITELCO'),
    ('NOKIA', 'NOKIA'),
    ('OSC', 'OSC'),
    ('WB INGENIERIA', 'WB INGENIERIA'),
    ('VOLUMEN', 'VOLUMEN'),
    ('INTELCOM', 'INTELCOM'),
    ('ASECONES', 'ASECONES'),
    ('SOI', 'SOI'),
    ('CONECTAR', 'CONECTAR'),
    ('IDT', 'IDT'),
    ('TECHMAHINDRA', 'TECHMAHINDRA'),
    ('ADS INTEGRAL', 'ADS INTEGRAL'),
    ('APPLUS', 'APPLUS'),
    ('CLARO', 'CLARO'),
    ('OIN (CLARO)', 'OIN (CLARO)'),
    ('SFERA', 'SFERA'),
    ('MSI', 'MSI'),
    ('YINDA', 'YINDA'),
    ('CELPLAN', 'CELPLAN'),
    ('RSE', 'RSE'),
    ('INMEL', 'INMEL'),
    ('CINCO', 'CINCO'),
    ('OPG', 'OPG'),
    ('NEWICT', 'NEWICT'),
    ('CAT', 'CAT'),
    ('STI', 'STI'),
    ('PRECOOM', 'PRECOOM'),
    ('CAM', 'CAM'),
    ('FUREL', 'FUREL'),
    ('ELETCOL', 'ELETCOL'),
    ('OFG', 'OFG'),
    ('SFERAONE', 'SFERAONE'),
    ('DYG', 'DYG'),
    ('MASTEC', 'MASTEC'),
    ('SOLINTEL', 'SOLINTEL'),
    ('PRODATEL', 'PRODATEL'),
    ('COMSA', 'COMSA'),
    ('ELECTRICA', 'ELECTRICA'),
)
