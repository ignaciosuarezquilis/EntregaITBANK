# Generated by Django 4.1 on 2022-09-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('codigopostal', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'sucursales',
            },
        ),
    ]
