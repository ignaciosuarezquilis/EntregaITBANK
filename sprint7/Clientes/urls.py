from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import ClienteDetails


urlpatterns=[
    path('home/',login_required(views.home),name='home'),
    #path('',login_required(views.home),name='home'),
    path('api/clientes/<int:pk>',ClienteDetails.as_view()),
]