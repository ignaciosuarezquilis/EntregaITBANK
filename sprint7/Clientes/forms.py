from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from Prestamos.models import Prestamo

class PrestamoForm(ModelForm):
    class Meta:
        model=Prestamo
        fields=['sucursal','tipo','user_id','total']