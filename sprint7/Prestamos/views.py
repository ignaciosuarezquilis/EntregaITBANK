from django.shortcuts import render,redirect
from .models import TipoPrestamo
from django.http import HttpResponse
from django.contrib import messages

import datetime
import locale

from django.http import request,HttpRequest,HttpResponse

from Cuentas.models import Cuenta, TipoCuenta
from .models import TipoPrestamo, Prestamo, MontoMax
from Clientes.models import Cliente,TipoCliente

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