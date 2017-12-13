# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0015_auto_20171012_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionnpo',
            name='posible_causa',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'Instalacion', b'Instalacion'), (b'Software', b'Software'), (b'Hardware', b'Hardware'), (b'Datafill', b'Datafill'), (b'Ajuste Potencia', b'Ajuste Potencia'), (b'Integracion', b'Integracion'), (b'Interferencia externa', b'Interferencia externa'), (b'Cambio diseno', b'Cambio diseno'), (b'Mal rechazo', b'Mal rechazo'), (b'Otra causa', b'Otra causa')], max_length=255, null=True),
        ),
    ]