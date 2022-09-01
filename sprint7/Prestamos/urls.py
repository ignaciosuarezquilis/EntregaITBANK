from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('loans/',login_required(views.loans),name='loans'),
]