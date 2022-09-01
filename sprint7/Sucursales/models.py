from django.db import models

# Create your models here.

class Sucursales(models.Model):
    id = models.IntegerField(primary_key=True,
                             editable=False,
                             )
    nombre = models.CharField(max_length=50)
    codigopostal=models.IntegerField()


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'sucursales'