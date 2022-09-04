from rest_framework import serializers
from .models import Prestamo
from django.contrib.auth.models import User

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        #indicamos que use todos los campos
        fields = "__all__"
        #les decimos cuales son los de solo lectura
        read_only_fields = (
        "id",
        "date",
        "tipo_id",
        "user_id",
        "total",
        "sucursal_id"
        )