# Generated by Django 4.1 on 2022-09-03 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0004_empleado_user'),
        ('Tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='cliente_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.cliente'),
            preserve_default=False,
        ),
    ]
