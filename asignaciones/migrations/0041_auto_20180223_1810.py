# Generated by Django 2.0 on 2018-02-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0040_auto_20180209_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionni',
            name='origen_falla',
            field=models.CharField(blank=True, choices=[('', '---------'), ('Instalacion', 'Instalacion'), ('Software', 'Software'), ('Hardware', 'Hardware'), ('Datafill', 'Datafill'), ('Ajuste Potencia', 'Ajuste Potencia'), ('Integracion', 'Integracion'), ('Interferencia externa', 'Interferencia externa'), ('Cambio diseno', 'Cambio diseno'), ('Mal rechazo', 'Mal rechazo'), ('TX', 'TX'), ('Comportamiento esperado', 'Comportamiento esperado'), ('Comportamiento previo', 'Comportamiento previo'), ('Ajuste Adyacencias', 'Ajuste Adyacencias')], max_length=255, null=True),
        ),
    ]
