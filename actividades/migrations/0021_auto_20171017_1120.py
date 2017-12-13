# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0020_auto_20171016_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='ni_estado',
            new_name='ni_estado_asignacion',
        ),
        migrations.RenameField(
            model_name='actividad',
            old_name='npo_estado',
            new_name='npo_estado_asignacion',
        ),
        migrations.AddField(
            model_name='actividad',
            name='fecha_estado_noc',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='degradacion',
            name='actividad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='degradaciones', to='actividades.Actividad'),
        ),
    ]