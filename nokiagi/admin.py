from django.contrib import admin
from .models import Gi

@admin.register(Gi)
class GiAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'wp',
    'agrupadores',
    'siteName',
    'region',
    'ciudad',
    'proyecto',
    'banda',
    'escenario',
    'ss',
    'realTiFinish',
    'fechaIntegracion',
    'fechaEstado',
    'estadoNOC',
    'subEstadoNOC',
    )
    search_fields = ['wp',]
