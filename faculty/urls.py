from . import views
from django.urls import path

app_name="faculty"

urlpatterns=[
    path('login_faculty',views.login_faculty,name="login_faculty"),
    path('forgotpwF',views.forgotpwF,name="forgotpwF"),
    path('faculty_home',views.faculty_home,name="faculty_home"),
    path('faculty_profile',views.faculty_profile,name="faculty_profile"),
    path('faculty_authentication',views.faculty_authentication,name="faculty_authentication"),
    path('student_register',views.student_register,name="student_register"),
    path('student_details',views.student_details,name="student_details"),
    path('search_student',views.search_student),
    path('attendance_date',views.attendance_date,name="attendance_date"),
    path('attendance_month',views.attendance_month,name="attendance_month"),
    path('faculty_msg',views.faculty_msg,name="faculty_msg"),
    path('faculty_chat_student',views.faculty_chat_student,name="faculty_chat_student"),
    path('faculty_chat_admin',views.faculty_chat_admin,name="faculty_chat_admin"),
]
