from django.shortcuts import render

# Create your views here.
def loginS(request):
    return render(request,'student/student_login.html')

def forgotpwS(request):
    return render(request,'student/student_forgot_pw.html')   

def profileS(request):
    return render(request,'student/student_profile.html')     

def authenticationS(request):
    return render(request,'student/student_authentication.html')    

def chatS(request):
    return render(request,'student/student_chat.html')     

