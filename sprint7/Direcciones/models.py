from pyexpat import model
from django.db import models
from Clientes.models import Cliente
from django.contrib.auth.models import User
# Create your models here.

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    calle=models.CharField(max_length=50)
    numero=models.IntegerField()
    codigopostal=models.CharField(max_length=50)

    class Meta:
        db_table = 'direcciones'

