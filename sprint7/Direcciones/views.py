
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

from .models import Direccion
from Clientes.models import Cliente
from .serializers import DireccionSerializer
from .forms import DireccionForm
from django.shortcuts import redirect, render

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


def updateDireccion(request,pk):
    direccion=Direccion.objects.get(id=pk)
    form=DireccionForm(instance=direccion)

    if request.method == 'POST':
        form=DireccionForm(request.POST,instance=direccion)
        if form.is_valid():
            form.save()
            return redirect('direcciones')

    context={'form':form}
    return render(request,'direcciones/direccionesform.html',context)