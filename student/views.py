from django.shortcuts import render

# Create your views here.
def loginS(request):
    return render(request,'student_login.html')