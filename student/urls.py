from . import views
from django.urls import path
app_name="student"


urlpatterns=[
    path('loginS',views.loginS,name="loginS"),
    path('registerS',views.registerS,name="registerS"),
    path('forgotpwS',views.forgotpwS,name="forgotpwS"),
]