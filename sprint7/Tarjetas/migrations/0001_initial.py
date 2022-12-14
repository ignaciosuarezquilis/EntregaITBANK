# Generated by Django 4.1 on 2022-08-30 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0003_empleado_alter_cliente_table_alter_tipocliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('tarjeta_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_tarjeta', models.CharField(max_length=20)),
                ('tarjeta_cvv', models.CharField(max_length=3)),
                ('tarjeta_fecha_de_otorgamiento', models.DateField()),
                ('tarjeta_fecha_de_expiracion', models.DateField()),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.cliente')),
            ],
            options={
                'db_table': 'tarjeta',
            },
        ),
    ]
