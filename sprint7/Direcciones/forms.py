from django.forms import ModelForm
from .models import Direccion

class DireccionForm(ModelForm):
    class Meta:
        model=Direccion
        fields=['calle','numero','codigopostal']
