# Generated by Django 3.1.2 on 2020-11-26 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20201122_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pedido', 'Pedido'), ('Enviar a taller', 'Enviar a taller'), ('Finalizado', 'Finalizado')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoría',
            field=models.CharField(choices=[('Lente', 'Lente'), ('Otro', 'Otro')], default='Otro', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripción',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.producto')),
            ],
            options={
                'unique_together': {('pedido', 'producto')},
            },
        ),
    ]
