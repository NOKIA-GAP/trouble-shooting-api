# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0007_auto_20171205_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='hardware',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'FSMF', b'FSMF'), (b'FPFD', b'FPFD'), (b'FTIF', b'FTIF'), (b'FXCB', b'FXCB'), (b'FXFC', b'FXFC'), (b'FRHG', b'FRHG'), (b'FRHD', b'FRHD'), (b'FRHC', b'FRHC'), (b'FTSI', b'FTSI'), (b'FSFC', b'FSFC'), (b'FYTG', b'FYTG'), (b'FSEB', b'FSEB'), (b'FSES', b'FSES'), (b'RET KIT', b'RET KIT'), (b'ANTENA', b'ANTENA'), (b'JUMPER', b'JUMPER'), (b'FEEDER', b'FEEDER'), (b'FIBRA', b'FIBRA'), (b'FILTRO', b'FILTRO')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudhw',
            name='estado_solicitud',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'Hardware solicitado', b'Hardware solicitado'), (b'Hardware recibido', b'Hardware recibido')], max_length=255, null=True),
        ),
    ]