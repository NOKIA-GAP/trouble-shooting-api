from django.db import models

class Gi(models.Model):
    # id = models.IntegerField(primary_key=True)
    wp = models.BigIntegerField(blank=True, null=True)
    agrupadores = models.CharField(max_length=255, blank=True, null=True)
    siteName = models.CharField(max_length=80, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    proyecto = models.CharField(max_length=19, blank=True, null=True)
    banda = models.CharField(max_length=30, blank=True, null=True)
    escenario = models.CharField(max_length=20, blank=True, null=True)
    ss = models.CharField(max_length=60, blank=True, null=True)
    onAir = models.DateField(blank=True, null=True)
    realTiFinish = models.DateField(blank=True, null=True)
    fechaIntegracion = models.DateField(blank=True, null=True)
    fechaEstado = models.DateTimeField(blank=True, null=True)
    estadoNOC = models.CharField(max_length=45, blank=True, null=True)
    subEstadoNOC = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # app_label = 'nokiagi'
        managed = False
        db_table = 'gi'
        verbose_name = "actividad"
        verbose_name_plural = "actividades"

    def __str__(self):
        return str(self.wp)
