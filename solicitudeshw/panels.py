from .models import SolicitudHW

REQUIEREHW = 'Requiere HW'
HWSOLICITADO = 'HW solicitado'
HWRECIBIDO = 'HW recibido'
CANCELADA = 'Cancelada'

solicitudeshw = SolicitudHW.objects.all()
solicitudeshw_hwrequrido = SolicitudHW.objects.filter(estado_solicitud=REQUIEREHW)
solicitudeshw_hwsolicitado = SolicitudHW.objects.filter(estado_solicitud=HWSOLICITADO)
solicitudeshw_hwrecibido = SolicitudHW.objects.filter(estado_solicitud=HWRECIBIDO)
solicitudeshw_hwcancelado = SolicitudHW.objects.filter(estado_solicitud=CANCELADA)
