# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0016_auto_20171010_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='ni_concepto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='ni_estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='ni_fecha_asignacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='ni_ingeniero',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='ni_tipo_intervencion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_concepto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_fecha_asignacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_ingeniero',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_posible_causa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actividad',
            name='npo_tipo_intervencion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
