from .models import Alerta

def alertas(request):
    alertas = Alerta.objects.all().count()
    return { 'alertas': alertas }
