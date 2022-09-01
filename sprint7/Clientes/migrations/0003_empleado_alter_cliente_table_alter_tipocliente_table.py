# Generated by Django 4.1 on 2022-08-30 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_alter_cliente_table_alter_tipocliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='CLIENTE',
        ),
        migrations.AlterModelTable(
            name='tipocliente',
            table='TIPO_CLIENTE',
        ),
    ]
