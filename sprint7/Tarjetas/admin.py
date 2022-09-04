from django.contrib import admin

from .models import Tarjeta, TipoTarjeta

# Register your models here.

admin.site.register(Tarjeta)
admin.site.register(TipoTarjeta)