from .models import (
Falla
)

INSTALACION = 'Instalacion'
INTEGRACION = 'Integracion'
SOFTWARE = 'Software'
HARDWARE = 'Hardware'
DATAFILL = 'Datafill'
AJUSTEPOTENCIA = 'Ajuste Potencia'
INTERFERENCIAEXTREMA = 'Interferencia externa'
CAMBIODISENO = 'Cambio diseno'
MALRECHAZO = 'Mal rechazo'
TX = 'TX'
COMPORTAMIENTOESPERADO = 'Comportamiento esperado'
COMPORTAMIENTOPREVIO = 'Comportamiento previo'
AJUSTEADYACENCIAS = 'Ajuste Adyacencias'

fallas = Falla.objects.all()
fallas_instalacion = Falla.objects.filter(tipo_falla=INSTALACION)
fallas_integracion = Falla.objects.filter(tipo_falla=INTEGRACION)
fallas_software = Falla.objects.filter(tipo_falla=SOFTWARE)
fallas_hardware = Falla.objects.filter(tipo_falla=HARDWARE)
fallas_datafill = Falla.objects.filter(tipo_falla=DATAFILL)
fallas_ajuste_potencia = Falla.objects.filter(tipo_falla=AJUSTEPOTENCIA)
fallas_interferencia_externa = Falla.objects.filter(tipo_falla=INTERFERENCIAEXTREMA)
fallas_cambio_diseno = Falla.objects.filter(tipo_falla=CAMBIODISENO)
fallas_mal_rechazo = Falla.objects.filter(tipo_falla=MALRECHAZO)
fallas_tx = Falla.objects.filter(tipo_falla=TX)
fallas_comportamiento_esperado = Falla.objects.filter(tipo_falla=COMPORTAMIENTOESPERADO)
fallas_comportamiento_previo = Falla.objects.filter(tipo_falla=COMPORTAMIENTOPREVIO)
fallas_ajuste_adyasencias = Falla.objects.filter(tipo_falla=AJUSTEADYACENCIAS)
