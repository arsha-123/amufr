from . import views
from django.urls import path


urlpatterns=[
    # path('',views.login,name="login")
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('login',views.login,name="login"),
    path('forgotpw',views.forgotpw,name="forgotpw"),
]