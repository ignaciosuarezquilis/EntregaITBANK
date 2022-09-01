from django.shortcuts import render
from .models import Sucursales
from .serializers import SucursalesSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

# Create your views here.

class SucursalDetails(APIView):
    def get(self,request):
        try:
            sucursales=Sucursales.objects.all()
            serializer=SucursalesSerializer(sucursales,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Sucursales.DoesNotExist:
            messages.error(request, 'No existen sucursales')
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)