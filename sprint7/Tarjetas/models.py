from django.db import models
from Clientes.models import Cliente

# Create your models here.

class TipoTarjeta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_tarjeta'

class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    tipotarjeta=models.ForeignKey(TipoTarjeta,on_delete=models.CASCADE, default=None, null=True)
    numero_tarjeta = models.CharField(max_length=20)
    tarjeta_cvv = models.CharField(max_length=3)
    tarjeta_fecha_de_otorgamiento = models.DateField()
    tarjeta_fecha_de_expiracion = models.DateField()
    user_id=models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        db_table = 'tarjeta'
