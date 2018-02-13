from .models import (
Actividad,
Degradacion
)

PRODUCCION = 'Produccion'
SEGUIMIENTO_12H ='Seguimiento 12h'
SEGUIMIENTO_24H = 'Seguimiento 24h'
SEGUIMIENTO_36H = 'Seguimiento 36h'


actividades = Actividad.objects.all()
actividades_estado_noc_produccion = Actividad.objects.filter(estado_noc=PRODUCCION)
actividades_estado_noc_seguimiento_12h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_12H)
actividades_estado_noc_seguimiento_24h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_24H)
actividades_estado_noc_seguimiento_36h = Actividad.objects.filter(estado_noc=SEGUIMIENTO_36H)
