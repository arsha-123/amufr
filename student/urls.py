from . import views
from django.urls import path

app_name="student"


urlpatterns=[
    path('login_student',views.login_student,name="login_student"),
    path('forgotpwS',views.forgotpwS,name="forgotpwS"),
    path('student_home',views.student_home,name="student_home"),
    path('student_profile',views.student_profile,name="student_profile"),
    path('student_authentication',views.student_authentication,name="student_authentication"),
    path('student_msg',views.student_msg,name="student_msg"),
    path('student_chat',views.student_chat,name="student_chat"),
]