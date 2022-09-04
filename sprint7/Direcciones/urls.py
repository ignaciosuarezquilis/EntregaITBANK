from django.urls import path
from . import views
from .views import DireccionDetails


urlpatterns=[
    path('api/direccionesxcliente/<int:pk>/',DireccionDetails.as_view(),name='direccionesxcliente'),
    path('modificardireccion/<int:pk>/',views.updateDireccion,name='modificardireccion'),
]