from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from .views import PrestamoDetails, PrestamoList, PrestamoPersonal, PrestamoRequest


urlpatterns=[
    path('loans/',login_required(views.loans),name='loans'),
    path('myloans/<int:pk>',PrestamoPersonal.as_view(),name='myloans'),
    path('api/prestamos/<int:pk>',login_required(PrestamoDetails.as_view()),name='eliminarprestamo'),
    path('api/prestamos/',PrestamoRequest.as_view(),name="solicitarprestamo"),
    path('api/prestamos/<int:pk>',PrestamoList.as_view(),name='verprestamo')
]