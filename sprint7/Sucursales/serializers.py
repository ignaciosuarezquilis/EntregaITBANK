from rest_framework import serializers
from .models import Sucursales

class SucursalesSerializer(serializers.Serializer):
    class Meta:
        model = Sucursales
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura