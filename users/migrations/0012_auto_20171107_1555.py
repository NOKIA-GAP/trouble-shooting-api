# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20171107_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ('creado',), 'permissions': (('perm_gap_administrador', 'Permisos para GAP Administrador'), ('perm_gap_visitante', 'Permisos para GAP Visitante'), ('perm_ni_ingeniero', 'Permisos para NI Ingeniero'), ('perm_ni_asignador', 'Permisos para NI Asignador'), ('perm_npo_ingeniero', 'Permisos para NPO Ingeniero'), ('perm_npo_asignador', 'Permisos para NPO Asignador'), ('perm_fm_lider', 'Permisos para FM Lider'), ('perm_fm_permisos', 'Permisos para FM Permisos'), ('perm_fm_supervisor', 'Permisos para FM Supervisor')), 'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
    ]