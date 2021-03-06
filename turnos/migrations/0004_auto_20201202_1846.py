# Generated by Django 3.1.2 on 2020-12-02 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_historial'),
        ('turnos', '0003_auto_20201202_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='médico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turnos.medico'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
        ),
    ]
