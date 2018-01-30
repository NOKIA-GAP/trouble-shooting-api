# Generated by Django 2.0 on 2018-01-29 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0045_auto_20180109_1128'),
        ('users', '0014_perfil_par'),
        ('estaciones', '0013_estacion_numero_actividades'),
        ('asignaciones', '0039_auto_20180124_1530'),
        ('notificaciones', '0003_auto_20180116_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionFallaAjustePotencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_ajuste_potencia', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_ajuste_potencia', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_ajuste_potencia', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_ajuste_potencia', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla ajuste potencia',
                'verbose_name_plural': 'notificaciones falla ajuste potencia',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaCambioDiseno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_cambio_diseno', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_cambio_diseno', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_cambio_diseno', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_cambio_diseno', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla cambio diseno',
                'verbose_name_plural': 'notificaciones falla cambio diseno',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaComportamientoEsperado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_comportamiento_esperado', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_comportamiento_esperado', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_comportamiento_esperado', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_comportamiento_esperado', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla comportamiento esperado',
                'verbose_name_plural': 'notificaciones falla comportamiento esperado',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaDatafill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_datafill', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_datafill', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_datafill', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_datafill', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla datafill',
                'verbose_name_plural': 'notificaciones falla datafill',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_hardware', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_hardware', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_hardware', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_hardware', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla hardware',
                'verbose_name_plural': 'notificaciones falla hardware',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaInterferenciaExterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_interferencia_externa', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_interferencia_externa', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_interferencia_externa', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_interferencia_externa', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla interferencia externa',
                'verbose_name_plural': 'notificaciones falla interferencia externa',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaMalRechazo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_mal_rechazo', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_mal_rechazo', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_mal_rechazo', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_mal_rechazo', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla mal rechazo',
                'verbose_name_plural': 'notificaciones falla mal rechazo',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_software', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_software', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_software', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_software', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla software',
                'verbose_name_plural': 'notificaciones falla software',
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='NotificacionFallaTX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp', models.BigIntegerField(blank=True, null=True)),
                ('service_supplier', models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI')], max_length=255, null=True)),
                ('banda', models.CharField(blank=True, max_length=255, null=True)),
                ('proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('escenario', models.CharField(blank=True, max_length=255, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_tx', to='actividades.Actividad')),
                ('asignacion_ni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_tx', to='asignaciones.AsignacionNi')),
                ('estacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_tx', to='estaciones.Estacion')),
                ('ni_ingeniero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_falla_tx', to='users.Perfil')),
            ],
            options={
                'verbose_name': 'notificacion falla TX',
                'verbose_name_plural': 'notificaciones falla TX',
                'ordering': ('creado',),
            },
        ),
    ]
