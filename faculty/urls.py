from . import views
from django.urls import path

app_name="faculty"

urlpatterns=[
    path('loginF',views.login_faculty,name="loginF"),
    path('forgotpwF',views.forgotpwF,name="forgotpwF"),
    path('profileF',views.profileF,name="profileF"),
    path('authenticationF',views.authenticationF,name="authenticationF"),
    path('registerS',views.registerS,name="registerS"),
    path('detailsS',views.detailsS,name="detailsS"),
    path('attendanceD',views.attendanceD,name="attendanceD"),
    path('attendanceM',views.attendanceM,name="attendanceM"),
]
