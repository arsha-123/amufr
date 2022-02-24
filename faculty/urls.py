from . import views
from django.urls import path
app_name="faculty"

urlpatterns=[
    path('loginF',views.login_faculty,name="loginF"),
    path('registerF',views.register,name="registerF"),
    path('forgotpwF',views.forgotpwF,name="forgotpwF")
]
