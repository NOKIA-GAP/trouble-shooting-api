# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='ciudad',
            field=models.CharField(choices=[(b'Bogota', b'Bogota'), (b'Cali', b'Cali'), (b'Medellin', b'Medellin'), (b'Bucaramanga', b'Bucaramanga'), (b'Barranquilla', b'Barranquilla'), (b'Cartagena', b'Cartagena')], max_length=255),
        ),
    ]