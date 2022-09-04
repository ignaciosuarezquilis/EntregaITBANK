from django.shortcuts import render
from .models import Sucursal
from .serializers import SucursalSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

# Create your views here.

class SucursalDetails(APIView):
    def get(self,request):
        try:
            sucursales=Sucursal.objects.all()
            serializer=SucursalSerializer(sucursales,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Sucursal.DoesNotExist:
            messages.error(request, 'No existen sucursales')
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)