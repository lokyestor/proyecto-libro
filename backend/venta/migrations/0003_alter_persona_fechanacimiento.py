# Generated by Django 5.0.4 on 2024-05-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_alter_direccion_table_alter_estadolibro_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(blank=True, db_column='fecha_nacimiento', null=True),
        ),
    ]
