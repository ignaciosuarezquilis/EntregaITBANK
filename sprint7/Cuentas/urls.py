from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required

from.views import CuentaDetails


urlpatterns=[
    path('api/accounts/<int:pk>',login_required(CuentaDetails.as_view()),name='accounts'),
]
