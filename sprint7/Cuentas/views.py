from django.shortcuts import render,redirect


from Cuentas.models import Cuenta, TipoCuenta
from Clientes.models import Cliente,TipoCliente

from django.contrib import messages

# Create your views here.
def accounts(request):
    context={}
    try:
            #context['tipocuentas']=TipoCuenta.objects.filter(id=Cuenta.objects.filter(customer_id=request.user.id).tipo_id)
            context['cuentas']=Cuenta.objects.filter(customer_id=request.user.id)

    except Cuenta.DoesNotExist:
            messages.error(request, 'No tiene cuentas registradas')
            return redirect('home')
    return render(request,'cuentas/profile.html',context)