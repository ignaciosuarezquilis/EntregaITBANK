from rest_framework import serializers
from .models import Cuenta
from django.contrib.auth.models import User

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
        "id",
        "balance",
        "tipo_id",
        "iban",
        "customer_id",
        )