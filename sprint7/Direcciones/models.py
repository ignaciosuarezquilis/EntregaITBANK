from pyexpat import model
from django.db import models
from Clientes.models import Cliente
# Create your models here.

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None, null=True)
    calle=models.CharField(max_length=50)
    numero=models.IntegerField()
    codigopostal=models.CharField(max_length=50)

    class Meta:
        db_table = 'direcciones'

