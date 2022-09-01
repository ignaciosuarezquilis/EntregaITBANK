# Generated by Django 4.1 on 2022-08-30 23:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_empleado_alter_cliente_table_alter_tipocliente_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoprestamo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Prestamos.tipoprestamo')),
            ],
            options={
                'db_table': 'prestamos',
            },
        ),
        migrations.CreateModel(
            name='MontoMax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(default=0)),
                ('tipo', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Clientes.tipocliente')),
            ],
            options={
                'db_table': 'MontoMax',
            },
        ),
    ]
