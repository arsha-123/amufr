from django.shortcuts import render

# Create your views here.
def login_faculty(request):
    return render(request,'faculty/faculty_login.html')

def forgotpwF(request):
    return render(request,'faculty/faculty_forgot_pw.html')

def profileF(request):
    return render(request,'faculty/faculty_profile.html')

def authenticationF(request):
    return render(request,'faculty/faculty_authentication.html')

def registerS(request):
    return render(request,'faculty/student_register.html')

def detailsS(request):
    return render(request,'faculty/student_details.html')

def attendanceD(request):
    return render(request,'faculty/student_attendanceD.html')

def attendanceM(request):
    return render(request,'faculty/student_attendanceM.html')














