# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 22:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividades', '0012_auto_20170928_1421'),
        ('users', '0004_auto_20170913_2204'),
        ('asignaciones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionConceptoNi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.IntegerField(blank=True, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='concepto_ni/imagen')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_ni', related_query_name='asignacion_conceptos_ni', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_ni', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_ni', to='estaciones.Estacion')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_ni', to='users.Perfil')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_ni', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('creado',),
                'verbose_name': 'concepto ni',
                'verbose_name_plural': 'conceptos ni',
            },
        ),
        migrations.CreateModel(
            name='AsignacionConceptoNpo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.IntegerField(blank=True, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='concepto_npo/imagen')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_npo', related_query_name='asignacion_conceptos_npo', to='actividades.Actividad')),
                ('asignacion_npo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_npo', to='asignaciones.AsignacionNpo')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_npo', to='estaciones.Estacion')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_npo', to='users.Perfil')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_conceptos_npo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('creado',),
                'verbose_name': 'concepto npo',
                'verbose_name_plural': 'conceptos npo',
            },
        ),
    ]
