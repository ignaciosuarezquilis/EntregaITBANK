from django.contrib import admin

from .models import  MontoMax, Prestamo, TipoPrestamo

# Register your models here.

admin.site.register(TipoPrestamo)
admin.site.register(Prestamo)
admin.site.register(MontoMax)
