# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0010_auto_20171207_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
