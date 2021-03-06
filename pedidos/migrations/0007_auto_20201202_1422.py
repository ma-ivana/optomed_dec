# Generated by Django 3.1.2 on 2020-12-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_auto_20201129_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('fecha_creación', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='pago',
            field=models.CharField(choices=[('Tarjeta de crédito', 'Tarjeta de crédito'), ('Tarjeta de débito', 'Tarjeta de débito'), ('Billetera virtual', 'Billetera virtual'), ('Efectivo', 'Efectivo')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.vendedor'),
        ),
    ]
