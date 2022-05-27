from . import views
from django.urls import path


urlpatterns=[
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('login',views.login,name="login"),
    path('forgotpw',views.forgotpw,name="forgotpw"),
    path('faculty_register',views.faculty_register,name="faculty_register"),
    path('profileA',views.profileA,name="profileA"),
    path('detailsSA',views.detailsSA,name="detailsSA"),

    path('search_stu',views.search_stu),
    
    path('detailsFA',views.detailsFA,name="detailsFA"),
    path('notificationsA',views.notificationsA,name="notificationsA"),
    path('view',views.view,name="view"),
]