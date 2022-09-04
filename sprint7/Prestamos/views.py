from django.shortcuts import render,redirect

from Clientes.models import Empleado
from .models import TipoPrestamo
from django.http import HttpResponse
from django.contrib import messages

import datetime
import locale

from django.http import request,HttpRequest,HttpResponse

from Cuentas.models import Cuenta, TipoCuenta
from .models import TipoPrestamo, Prestamo, MontoMax
from Clientes.models import Cliente,TipoCliente

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import PrestamoSerializer

# Create your views here.

def loans(request):
    context={}
    if request.method == "POST":
        return formulario(request)

    tipos=TipoPrestamo.objects.all()
    context['tipos'] = tipos
    return render(request,'prestamos/prestamos.html',context)


def formulario(request):
    
    errors=False

    tipo = request.POST.get('tipo')

    tipo_cliente=Cliente.objects.get(user_id=request.user.id)
    idtipo_cliente=(TipoCliente.objects.get(id=tipo_cliente.tipo_id)).id




    fecha = datetime.datetime.strptime(request.POST.get('fecha'), '%Y-%m-%d')
    monto = float(request.POST.get('monto'))

    user = request.user

    try:
        tipo_cuenta = TipoCuenta.objects.get(nombre="Caja de ahorro en pesos")
        cuenta = Cuenta.objects.get(customer_id=user, tipo_id=tipo_cuenta)

        try:
            monto_max = MontoMax.objects.get(tipo_id=idtipo_cliente)
            print(monto_max.monto)
            print(TipoCliente.objects.get(id=tipo_cliente.tipo_id))
        except MontoMax.DoesNotExist:
            monto_max = MontoMax(monto=0)

        if monto > monto_max.monto:
            messages.error(request, f'El monto no puede ser mayor a: {str(monto_max)}')
            errors = True
        else:
            cuenta.balance = cuenta.balance + monto
    except TipoCuenta.DoesNotExist:
        messages.error(request, 'No existe el tipo Cuenta de Ahorro')
        errors = True
    except Cuenta.DoesNotExist:
        messages.error(request, 'No existe una CA para el Usuario')
        errors = True
    except Cuenta.MultipleObjectsReturned:
        messages.error(request, 'Existe mas de una cuenta de ahorro para el usuario')
        errors = True

    if errors is False:
        cuenta.save()
        prestamo = Prestamo(tipo_id=tipo, date=fecha, total=monto, cliente=user)
        prestamo.save()
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        messages.success(request, f'Prestamo de {locale.currency(prestamo.total, grouping=True)} solicitado')
        return redirect('home')
    else:
        return redirect('loans')


class PrestamoPersonal(APIView):
    def get(self,request,pk):
        try:
            context={}    
            prestamos=Prestamo.objects.filter(user_id=request.user.id)
            serializer = PrestamoSerializer(prestamos, many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Prestamo.DoesNotExist:
            messages.error(request, 'No existen prestamos vinculados a esta cuenta')
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class PrestamoList(APIView):
    def get(self,request,pk):
        es_empleado=Empleado.objects.get(user_id=request.user.id)
        if  es_empleado:
            prestamos=Prestamo.objects.filter(user_id=pk)
            serializer=PrestamoSerializer(prestamos,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class PrestamoDetails(APIView):   
    def delete(self, request, pk):
        try:
            #borra un prestamo con un id determinado
            prestamo = Prestamo.objects.get(id=pk)
            es_empleado=Empleado.objects.get(user_id=request.user.id)
            cuenta=Cuenta.objects.get(customer_id=prestamo.user_id,tipo_id=1)
            print(cuenta.balance)
            cuenta.balance=cuenta.balance-prestamo.total
            cuenta.save()
            print(cuenta.balance)
            serializer = PrestamoSerializer(prestamo)
            prestamo.delete()
            return redirect('prestamos')
        except Prestamo.DoesNotExist:
            messages.error(request, 'No existe el prestamo')
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Empleado.DoesNotExist:
            messages.error(request, 'No tiene permisos')
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Cuenta.DoesNotExist:
             messages.error(request, 'El prestamo a eliminar no tiene una cuenta asociada')
             return Response(status=status.HTTP_404_NOT_FOUND)


class PrestamoRequest(APIView):
    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  