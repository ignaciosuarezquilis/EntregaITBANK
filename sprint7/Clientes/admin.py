from django.contrib import admin

from .models import Cliente, Empleado, TipoCliente

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(TipoCliente)
