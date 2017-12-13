# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171019_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='empresa',
            field=models.CharField(blank=True, choices=[(b'DECOM', b'DECOM'), (b'INGETEL', b'INGETEL'), (b'ENECON', b'ENECON'), (b'NEXPRO', b'NEXPRO'), (b'JANACOR', b'JANACOR'), (b'UNION', b'UNION'), (b'OPTIMACOM', b'OPTIMACOM'), (b'DELTEC', b'DELTEC'), (b'FIBRATERRA', b'FIBRATERRA'), (b'ADSM', b'ADSM'), (b'SERVINTELCO', b'SERVINTELCO'), (b'EZENTIS', b'EZENTIS'), (b'SITCOM', b'SITCOM'), (b'INGYTELCOM', b'INGYTELCOM'), (b'SAI', b'SAI'), (b'GAMMA', b'GAMMA'), (b'PACIFIC ENERGY', b'PACIFIC ENERGY'), (b'FUREL', b'FUREL'), (b'NEOSTAR', b'NEOSTAR'), (b'DASCON', b'DASCON'), (b'ATENA', b'ATENA'), (b'ZOOM', b'ZOOM'), (b'LINEA', b'LINEA'), (b'WISECA', b'WISECA'), (b'REDES Y SERVICIOS', b'REDES Y SERVICIOS'), (b'NESITELCO', b'NESITELCO'), (b'NOKIA', b'NOKIA'), (b'OSC', b'OSC'), (b'MSI', b'MSI'), (b'WB INGENIERIA', b'WB INGENIERIA'), (b'VOLUMEN', b'VOLUMEN'), (b'INTELCOM', b'INTELCOM'), (b'ASECONES', b'ASECONES'), (b'SOI', b'SOI'), (b'CONECTAR', b'CONECTAR'), (b'IDT', b'IDT'), (b'TECHMAHINDRA', b'TECHMAHINDRA'), (b'ADS INTEGRAL', b'ADS INTEGRAL'), (b'APPLUS', b'APPLUS'), (b'CLARO', b'CLARO'), (b'OIN (CLARO)', b'OIN (CLARO)'), (b'SFERA', b'SFERA')], max_length=255, null=True),
        ),
    ]
