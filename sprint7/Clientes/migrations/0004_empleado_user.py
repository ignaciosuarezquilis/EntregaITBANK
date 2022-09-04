# Generated by Django 4.1 on 2022-09-02 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clientes', '0003_empleado_alter_cliente_table_alter_tipocliente_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
