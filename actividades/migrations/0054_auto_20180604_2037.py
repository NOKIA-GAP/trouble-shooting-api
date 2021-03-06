# Generated by Django 2.0 on 2018-06-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0053_auto_20180403_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='clasificacion_previa',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='service_supplier',
            field=models.CharField(blank=True, choices=[('DECOM', 'DECOM'), ('INGETEL', 'INGETEL'), ('ENECON', 'ENECON'), ('NEXPRO', 'NEXPRO'), ('JANACOR', 'JANACOR'), ('UNION', 'UNION'), ('OPTIMACOM', 'OPTIMACOM'), ('DELTEC', 'DELTEC'), ('FIBRATERRA', 'FIBRATERRA'), ('ADSM', 'ADSM'), ('SERVINTELCO', 'SERVINTELCO'), ('EZENTIS', 'EZENTIS'), ('SITCOM', 'SITCOM'), ('INGYTELCOM', 'INGYTELCOM'), ('SAI', 'SAI'), ('GAMMA', 'GAMMA'), ('PACIFIC ENERGY', 'PACIFIC ENERGY'), ('FUREL', 'FUREL'), ('NEOSTAR', 'NEOSTAR'), ('DASCON', 'DASCON'), ('ATENA', 'ATENA'), ('ZOOM', 'ZOOM'), ('LINEA', 'LINEA'), ('WISECA', 'WISECA'), ('REDES Y SERVICIOS', 'REDES Y SERVICIOS'), ('NESITELCO', 'NESITELCO'), ('NOKIA', 'NOKIA'), ('OSC', 'OSC'), ('WB INGENIERIA', 'WB INGENIERIA'), ('VOLUMEN', 'VOLUMEN'), ('INTELCOM', 'INTELCOM'), ('ASECONES', 'ASECONES'), ('SOI', 'SOI'), ('CONECTAR', 'CONECTAR'), ('IDT', 'IDT'), ('TECHMAHINDRA', 'TECHMAHINDRA'), ('ADS INTEGRAL', 'ADS INTEGRAL'), ('APPLUS', 'APPLUS'), ('CLARO', 'CLARO'), ('OIN (CLARO)', 'OIN (CLARO)'), ('SFERA', 'SFERA'), ('MSI', 'MSI'), ('YINDA', 'YINDA'), ('CELPLAN', 'CELPLAN'), ('RSE', 'RSE'), ('INMEL', 'INMEL'), ('CINCO', 'CINCO'), ('OPG', 'OPG'), ('NEWICT', 'NEWICT'), ('CAT', 'CAT'), ('STI', 'STI'), ('PRECOOM', 'PRECOOM')], max_length=255, null=True),
        ),
    ]
