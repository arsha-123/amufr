from . import views
from django.urls import path

urlpatterns=[
    path('loginS',views.loginS,name="loginS")
]