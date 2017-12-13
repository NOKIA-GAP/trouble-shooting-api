# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0011_auto_20171011_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionni',
            name='estado',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'Asignada', b'Asignada'), (b'No exitosa', b'No exitosa'), (b'Enviado a seguimiento', b'Enviado a seguimiento'), (b'Requiere visita', b'Requiere visita'), (b'En monitoreo', b'En monitoreo'), (b'Escalado a claro', b'Escalado a claro')], default='Asignada', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asignacionnpo',
            name='estado',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'Asignada', b'Asignada'), (b'No exitosa', b'No exitosa'), (b'Enviado a seguimiento', b'Enviado a seguimiento'), (b'Requiere visita', b'Requiere visita'), (b'En monitoreo', b'En monitoreo'), (b'Escalado a claro', b'Escalado a claro')], default='Asignada', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asignacionnpo',
            name='posible_causa',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'Instalacion', b'Instalacion'), (b'Software', b'Software'), (b'Hardware', b'Hardware'), (b'Datafill', b'Datafill'), (b'Ajuste Potencia', b'Ajuste Potencia'), (b'Integracion', b'Integracion'), (b'Interferncia externa', b'Interferncia externa'), (b'Cambio dise\xc3\xb1o', b'Cambio dise\xc3\xb1o'), (b'Mal rechazo', b'Mal rechazo')], max_length=255, null=True),
        ),
    ]
