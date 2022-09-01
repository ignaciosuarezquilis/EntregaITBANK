from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('accounts/',login_required(views.accounts),name='accounts'),
]
