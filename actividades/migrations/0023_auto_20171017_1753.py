# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0022_auto_20171017_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ('creado',), 'permissions': (('perm_gap_administrador', 'Permisos para GAP Administrador'), ('perm_ni_ingeniero', 'Permisos para NI Ingeniero'), ('perm_ni_asignador', 'Permisos para NI Asignador'), ('perm_npo_ingeniero', 'Permisos para NPO Ingeniero'), ('perm_npo_asignador', 'Permisos para NPO Asignador'), ('perm_fm_lider', 'Permisos para FM Lider'), ('perm_fm_permisos', 'Permisos para FM Permisos'), ('perm_fm_supervisor', 'Permisos para FM Supervisor')), 'verbose_name': 'actividad', 'verbose_name_plural': 'actividades'},
        ),
        migrations.AddField(
            model_name='actividad',
            name='service_supplier',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
