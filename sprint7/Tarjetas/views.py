from django.shortcuts import render,redirect

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

from .models import Tarjeta
from Clientes.models import Cliente,Empleado
from .serializers import TarjetaSerializer


# Create your views here.

def isAutorizado(request,pk):
    try:
        esempleado=Empleado.objects.get(user_id=request.user.id)
        return True
    except Empleado.DoesNotExist:
        if(request.user.id==pk):
            return True
        else:
            return False
    

class TarjetaDetails(APIView):
    def get(self, request, pk):
        if(isAutorizado(request,pk)):        
            tarjetas = Tarjeta.objects.filter(user_id=pk,tipotarjeta=1)
            serializer = TarjetaSerializer(tarjetas,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            messages.error(request, 'No tiene acceso, no es un empleado registrado o cliente autorizado')
            return redirect('home')

            