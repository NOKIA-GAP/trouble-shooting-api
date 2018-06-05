# Generated by Django 2.0 on 2018-06-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0041_auto_20180223_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionni',
            name='clasificacion_previa',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Instalacion', 'Instalacion'), ('Quality', 'Quality'), ('Perdida de Trafico', 'Perdida de Trafico'), ('Denied/Drop', 'Denied/Drop'), ('Software', 'Software'), ('Handover', 'Handover'), ('Configuracion', 'Configuracion'), ('Mal Rechazo', 'Mal Rechazo')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='asignacionni',
            name='hardware_propietario',
            field=models.CharField(blank=True, choices=[('', '---------'), ('NOKIA', 'NOKIA'), ('CLARO', 'CLARO'), ('TERCEROS', 'TERCEROS')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='asignacionni',
            name='origen_falla',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Instalacion', 'Instalacion'), ('Software', 'Software'), ('Hardware', 'Hardware'), ('Datafill', 'Datafill'), ('Ajuste Potencia', 'Ajuste Potencia'), ('Integracion', 'Integracion'), ('Interferencia externa', 'Interferencia externa'), ('Cambio diseno', 'Cambio diseno'), ('Mal rechazo', 'Mal rechazo'), ('TX', 'TX'), ('Falla Externa', 'Falla Externa'), ('Falla TSS', 'Falla TSS'), ('Ajuste Adyacencias', 'Ajuste Adyacencias')], max_length=255, null=True),
        ),
    ]
