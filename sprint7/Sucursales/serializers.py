from rest_framework import serializers
from .models import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura