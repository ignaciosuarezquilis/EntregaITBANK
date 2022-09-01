from django.urls import path
from . import views
from .views import SucursalDetails


urlpatterns=[
    path('api/sucursales/',SucursalDetails.as_view()),
]