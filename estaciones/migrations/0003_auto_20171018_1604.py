# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0002_auto_20171002_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='regional',
            field=models.CharField(choices=[(b'Centro', b'Centro'), (b'Costa', b'Costa'), (b'Nor Occidente', b'Nor Occidente'), (b'Nor Oriente', b'Nor Oriente'), (b'Sur Occidente', b'Sur Occidente')], max_length=255),
        ),
    ]
