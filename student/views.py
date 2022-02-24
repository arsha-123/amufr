from django.shortcuts import render

# Create your views here.
def loginS(request):
    return render(request,'student_login.html')

def registerS(request):
    return render(request,'student_register.html')

def forgotpwS(request):
    return render(request,'student_forgot_pw.html')    