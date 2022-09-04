from rest_framework import serializers
from .models import Direccion


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura