from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    password1=forms.CharField(label='Contrasena',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar contrasena',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password1','password2']