# Generated by Django 2.0 on 2018-01-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0033_auto_20180109_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionni',
            name='detalle_falla_instalacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
