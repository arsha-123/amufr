from django.shortcuts import render

# Create your views here.
def login_faculty(request):
    return render(request,'faculty_login.html')

def register(request):
    return render(request,'faculty_register.html')

def forgotpwF(request):
    return render(request,'faculty_forgot_pw.html')