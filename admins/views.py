from django.shortcuts import render

# Create your views here.
# def login(request):
#     return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def login(request):
    return render(request,'login.html')

def forgotpw(request):
    return render(request,'admin_forgot_pw.html')