from rest_framework import serializers
from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura