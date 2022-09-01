from email import contentmanager
from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClienteSerializer


from .models import Cliente,TipoCliente

from django.contrib import messages

# Create your views here.
def home(request):
    context={}
    tipo_cliente=Cliente.objects.get(user_id=request.user.id)
    nombretipo_cliente=(TipoCliente.objects.get(id=tipo_cliente.tipo_id)).nombre


    context['nombretipocliente']=nombretipo_cliente
    return render(request,'extra/home.html',context)

class ClienteDetails(APIView):
    def get(self,request,pk):

        try:
            cliente=Cliente.objects.get(user_id=pk)
            serializer=ClienteSerializer(cliente)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            messages.error(request, 'No existe el cliente')
            return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
