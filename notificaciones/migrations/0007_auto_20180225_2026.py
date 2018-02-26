# Generated by Django 2.0 on 2018-02-26 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0006_auto_20180223_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacionfallaajustepotencia',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallaajustepotencia',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallaajustepotencia',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallaajustepotencia',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacambiodiseno',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacambiodiseno',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacambiodiseno',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacambiodiseno',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoesperado',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoesperado',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoesperado',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoesperado',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoprevio',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoprevio',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoprevio',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallacomportamientoprevio',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfalladatafill',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfalladatafill',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfalladatafill',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfalladatafill',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallahardware',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallahardware',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallahardware',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallahardware',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallainterferenciaexterna',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallainterferenciaexterna',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallainterferenciaexterna',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallainterferenciaexterna',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallamalrechazo',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallamalrechazo',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallamalrechazo',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallamalrechazo',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallasoftware',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallasoftware',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallasoftware',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallasoftware',
            name='ni_ingeniero',
        ),
        migrations.RemoveField(
            model_name='notificacionfallatx',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='notificacionfallatx',
            name='asignacion_ni',
        ),
        migrations.RemoveField(
            model_name='notificacionfallatx',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='notificacionfallatx',
            name='ni_ingeniero',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaAjustePotencia',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaCambioDiseno',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaComportamientoEsperado',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaComportamientoPrevio',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaDatafill',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaHardware',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaInterferenciaExterna',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaMalRechazo',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaSoftware',
        ),
        migrations.DeleteModel(
            name='NotificacionFallaTX',
        ),
    ]