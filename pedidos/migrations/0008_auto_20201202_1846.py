# Generated by Django 3.1.2 on 2020-12-02 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_historial'),
        ('pedidos', '0007_auto_20201202_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.vendedor'),
        ),
    ]
