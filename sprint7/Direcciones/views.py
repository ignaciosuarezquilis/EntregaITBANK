
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

from .models import Direccion
from Clientes.models import Cliente
from .serializers import DireccionSerializer

# Create your views here.

class DireccionDetails(APIView):
    def put(self, request, pk):
        #vamos a la direccion que queremos modificar
        cliente=Cliente.objects.get(user_id=request.user.id)
        direccion = Direccion.objects.get(cliente_id=cliente.id)
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)