# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0028_auto_20171020_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='estado_ultimo',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='estado_unico',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
