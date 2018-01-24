from django.db import models
from django.urls import reverse
from estaciones.models import Estacion
from actividades.models import Actividad
from incidentes.models import IncidenteNpo, IncidenteNi
from users.models import Perfil

class ComentarioNpo(models.Model):
    npo_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    incidente_npo = models.ForeignKey(IncidenteNpo, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    wp = models.BigIntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "comentario npo"
        verbose_name_plural = "comentarios npo"

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse('comentarios:detail_comentario_npo', kwargs={'pk': self.pk})

class ComentarioNi(models.Model):
    npo_ingeniero = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    incidente_npo = models.ForeignKey(IncidenteNi, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios_npo')
    wp = models.BigIntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=False)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "comentario ni"
        verbose_name_plural = "comentarios ni"

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse('comentarios:detail_comentario_ni', kwargs={'pk': self.pk})
