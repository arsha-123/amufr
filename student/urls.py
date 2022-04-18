from . import views
from django.urls import path
app_name="student"


urlpatterns=[
    path('loginS',views.loginS,name="loginS"),
    path('forgotpwS',views.forgotpwS,name="forgotpwS"),
    path('profileS',views.profileS,name="profileS"),
    path('authenticationS',views.authenticationS,name="authenticationS"),
    path('chatS',views.chatS,name="chatS"),
]