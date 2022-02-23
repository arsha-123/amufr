from . import views
from django.urls import path

urlpatterns=[
    path('loginF',views.loginF,name="loginF")
]