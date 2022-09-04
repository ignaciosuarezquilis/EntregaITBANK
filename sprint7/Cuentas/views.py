from django.shortcuts import render,redirect


from Cuentas.models import Cuenta, TipoCuenta
from Clientes.models import Cliente,TipoCliente
from .serializers import CuentaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib import messages

# Create your views here.
#def accounts(request):
    #context={}
    #try:
            #(Cuenta.objects.filter(customer_id=request.user.id)).objects.map()
            #context['tipocuentas']=TipoCuenta.objects.filter(id=Cuenta.objects.filter(customer_id=request.user.id).tipo_id)
            #context['cuentas']=Cuenta.objects.filter(customer_id=request.user.id)

    #except Cuenta.DoesNotExist:
            #messages.error(request, 'No tiene cuentas registradas')
            #return redirect('home')
    #return render(request,'cuentas/profile.html',context)

class CuentaDetails(APIView):
    def get(self,request,pk):

        try:
            if(pk==request.user.id):
                cuentas=Cuenta.objects.filter(customer_id=pk)
                serializer=CuentaSerializer(cuentas,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                messages.error(request, 'No tiene permisos')
                return redirect('home')
        except Cuenta.DoesNotExist:
            messages.error(request, 'No tiene cuentas asociadas')
            return redirect('home')
            #return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)  