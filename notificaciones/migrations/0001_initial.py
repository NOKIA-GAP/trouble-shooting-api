# Generated by Django 2.0 on 2018-01-14 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asignaciones', '0036_asignacionni_detalle_solicitud_visita'),
        ('users', '0014_perfil_par'),
        ('actividades', '0045_auto_20180109_1128'),
        ('estaciones', '0011_auto_20171224_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionFallaInstalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('service_supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('detalle_falla_instalacion', models.TextField(blank=True, null=True)),
                ('solver', models.CharField(blank=True, choices=[('', '---------'), ('Nokia', 'Nokia'), ('Service suplier', 'Service suplier')], max_length=255, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_instalacion', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_instalacion', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_instalacion', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_instalacion', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla instalacion',
                'verbose_name_plural': 'notificaciones falla instalacion',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaIntegracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('service_supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_integracion', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_integracion', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_integracion', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_integracion', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla integracion',
                'verbose_name_plural': 'notificaciones falla integracion',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionRequiereVisita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('service_supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('detalle_solicitud_visita', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_requiere_visita', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_requiere_visita', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_requiere_visita', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_requiere_visita', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion requiere visita',
                'verbose_name_plural': 'notificaciones requiere visita',
                'ordering': ('creado',),
            },
        ),
    ]
