from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import ClienteDetails, PrestamoDetails


urlpatterns=[
    path('home/',login_required(views.home),name='home'),
    #path('',login_required(views.home),name='home'),
    #path('empleado/',login_required(views.empleado),name='empleado'),
    path('sucursales/',login_required(views.sucursalesprestamos),name='sucursalesprestamos'),
    path('tarjetas/',login_required(views.tarjetas),name='tarjetas'),
    path('direcciones/',login_required(views.direcciones),name='direcciones'),
    path('prestamos/',login_required(views.prestamos),name='prestamos'),
    path('solicitarprestamos/',login_required(views.solicitarprestamos),name='solicitarprestamosform'),
    path('api/clientes/<int:pk>',ClienteDetails.as_view(),name='infocliente'),
    path('api/perstamosxsucursal/<int:pk>',PrestamoDetails.as_view(),name='prestamosxsucursal'),
]