# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import ReporteActividad
from users.models import Perfil
from django.core.mail import send_mail as _send_mail
from django.core.mail import EmailMessage
from .resources import ReporteActividadResource
from django.http import HttpResponse


class ReporteActividadForm(ModelForm):
    gap_administrador = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Perfil.objects.filter(perfil_usuario='GAP Administrador'), required=True)

    class Meta:
        model = ReporteActividad
        fields = ('gap_administrador',)


    # def send_email(self):
    #     cleaned_data = super(ReporteActividadForm, self).clean()
    #     gap_administrador = cleaned_data.get('gap_administrador')
    #     email = EmailMessage(
    #     'Reporte Actividad',
    #     'contenido',
    #     'reportes@troubleshooting.com',
    #     ['jucebridu@gmail.com'],
    #     )
    #     reporte_actividad_resource = ReporteActividadResource()
    #     file_name = 'ReporteActividad.xlsx'
    #     dataset = reporte_actividad_resource.export()
    #     email.attach(file_name, dataset.xlsx, mimetype='application/vnd.ms-excel')
    #     email.send(fail_silently=False)


    # def export_reporte_actividad(self):
    #     reporte_actividad_resource = ReporteActividadResource()
    #     dataset = reporte_actividad_resource.export()
    #     response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    #     response['Content-Disposition'] = 'attachment; filename="ReporteActividad.xlsx"'
    #     return response

    # def delete_reporte_actividad(self):
    #     reporte_actividades = ReporteActividad.objects.all()
    #     for reporte_actividad in reporte_actividades:
    #         reporte_actividad.delete()
