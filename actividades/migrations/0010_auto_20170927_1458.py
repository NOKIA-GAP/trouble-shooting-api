# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0009_auto_20170926_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='agrupador',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='banda',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='ciudad',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='escenario',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='estacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='estaciones.Estacion'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='proyecto',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='regional',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='responsable_actual',
            field=models.CharField(blank=True, choices=[(b'', b'---------'), (b'NI', b'NI'), (b'NPO', b'NPO'), (b'Optimizacion', b'Optimizacion')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='valor_wp_eur',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='wp',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]