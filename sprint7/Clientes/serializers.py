from rest_framework import serializers

from Prestamos.models import Prestamo
from .models import Cliente
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
        "id",
        "customer_DNI",
        "tipo_id",
        "user_id",
        )
