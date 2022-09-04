from cgi import print_form
from email import contentmanager
from urllib import response
from django.shortcuts import redirect, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from Direcciones.models import Direccion


from .serializers import ClienteSerializer
from Prestamos.serializers import PrestamoSerializer

from Sucursales.models import Sucursal

from Prestamos.models import Prestamo
from .models import Cliente,Empleado

from django.contrib import messages
from Clientes.models import Cliente

from Cuentas.models import Cuenta

from .forms import PrestamoForm

# Create your views here.
def home(request):
    context={}
    try:
        empleado=Empleado.objects.get(user_id=request.user.id)
        return render(request,'extra/empleados/empleado.html',context)
    except Empleado.DoesNotExist:
        return render(request,'extra/home.html',context)


    #empleado=Empleado.objects.get(user_id=request.user.id)
    #tipo_cliente=Cliente.objects.get(user_id=request.user.id)
    #nombretipo_cliente=(TipoCliente.objects.get(id=tipo_cliente.tipo_id)).nombre


    #context['nombretipocliente']=nombretipo_cliente
    #return render(request,'extra/home.html',context)

def sucursalesprestamos(request):
    context={}
    sucursales=Sucursal.objects.all()
    context['sucursales']=sucursales
    return render(request,'extra/empleados/sucursales.html',context)

def tarjetas(request):
    context={}
    clientes=Cliente.objects.all()
    context['clientes']=clientes
    return render(request,'extra/empleados/tarjetas.html',context)

def direcciones(request):
    context={}
    direcciones=Direccion.objects.all()
    context['direcciones']=direcciones
    return render(request,'extra/empleados/direcciones.html',context)

def prestamos(request):
    context={}
    prestamos=Prestamo.objects.all()
    context['prestamos']=prestamos
    return render(request,'extra/empleados/prestamos.html',context)

def solicitarprestamos(request):
    form=PrestamoForm()
    if request.method=='POST':
        form=PrestamoForm(request.POST)
        if form.is_valid():
            print('La request POST es: ',request.POST)
            cuenta=Cuenta.objects.get(customer_id=request.POST.user_id,tipo_id=1)
            cuenta.balance=cuenta.balance+form.total
            form.save()
            cuenta.save()
            return redirect ('prestamos')
    context={'form':form}
    return render(request,'extra/empleados/solicitarprestamo.html',context)


def empleado(request):
    return render(request,'extra/empleados/empleado.html')

class ClienteDetails(APIView):
    def get(self,request,pk):

        try:
            if(pk==request.user.id):
                cliente=Cliente.objects.get(user_id=pk)
                serializer=ClienteSerializer(cliente)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                messages.error(request, 'No tiene permisos')
                return redirect('home')
        except Cliente.DoesNotExist:
            messages.error(request, 'No existe el cliente')
            return redirect('login')
            #return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
            # 

class PrestamoDetails(APIView):
    def get(self,request,pk):

        try:
            esempleado=Empleado.objects.get(user_id=request.user.id)
            prestamos=Prestamo.objects.filter(sucursal_id=pk)
            serializer=PrestamoSerializer(prestamos,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Empleado.DoesNotExist:
            messages.error(request, 'No tiene acceso, no es un empleado registrado')
            return redirect('home')


