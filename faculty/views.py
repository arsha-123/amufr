from django.shortcuts import render

# Create your views here.
def loginF(request):
    return render(request,'faculty_login.html')