from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'admins/home.html')

def contact(request):
    return render(request,'admins/contact.html')

def about(request):
    return render(request,'admins/about.html')

def services(request):
    return render(request,'admins/services.html')

def login(request):
    return render(request,'admins/login.html')

def forgotpw(request):
    return render(request,'admins/admin_forgot_pw.html')

def registerF(request):
    return render(request,'admins/faculty_register.html')

def profileA(request):
    return render(request,'admins/admin_profile.html')

def detailsSA(request):
    return render(request,'admins/admins_student_details.html')

def detailsFA(request):
    return render(request,'admins/admins_faculty_details.html')

def notificationsA(request):
    return render(request,'admins/admins_notifications.html')

def view(request):
    return render(request,'admins/view.html')