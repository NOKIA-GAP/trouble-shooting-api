from .models import SolicitudHW

REQUIEREHW = 'Requiere HW'
HWSOLICITADO = 'HW solicitado'
HWRECIBIDO = 'HW recibido'
CANCELADA = 'Cancelada'

solicitudeshw = SolicitudHW.objects.all()
solicitudeshw_hwrequrido = solicitudeshw.filter(estado_solicitud=REQUIEREHW)
solicitudeshw_hwsolicitado = solicitudeshw.filter(estado_solicitud=HWSOLICITADO)
solicitudeshw_hwrecibido = solicitudeshw.filter(estado_solicitud=HWRECIBIDO)
solicitudeshw_hwcancelado = solicitudeshw.filter(estado_solicitud=CANCELADA)
