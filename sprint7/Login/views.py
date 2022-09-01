from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm




# Create your views here.

def register(request):
        if request.method == 'POST':
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data['username']
                messages.success(request,f'Usuario {username} creado')
                return redirect('home')
        else:
            form=UserRegisterForm()

        context={'form':form}
        return render(request,'social/register.html',context)

