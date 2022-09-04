from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required

from.views import TarjetaDetails


urlpatterns=[
    path('api/tarjetas/<int:pk>',login_required(TarjetaDetails.as_view()),name='tarjetasxcliente'),
]
