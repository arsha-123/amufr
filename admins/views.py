from django.shortcuts import render,redirect

from admins.models import Admin, Faculty
from admins.models import Faculty
from faculty.models import Student


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
    error=''
    if request.method=='POST':
        a_email=request.POST['ad_email']
        a_password=request.POST['ad_password']
        print(a_password, a_email)
        try:
            user_data=Admin.objects.get(email=a_email)
            print(user_data.email, user_data.password)
            if user_data.email == a_email and user_data.password == a_password:
                request.session['admin_id']=user_data.id
                return redirect('profileA')
            else:
                error="invalid username or password"

        except Exception:
            return redirect('login')

    return render(request,'admins/login.html',{'error':error})

    

def forgotpw(request):
    return render(request,'admins/admin_forgot_pw.html')

def faculty_register(request):
    if request.method=='POST':
        fac_name=request.POST['f_name']
        fac_dpt=request.POST['f_dpt']
        fac_gender=request.POST['f_gender']
        fac_dob=request.POST['f_dob']
        fac_email=request.POST['f_email']
        fac_phone=request.POST['f_phone']
        fac_password=request.POST['f_password']

        fac_obj=Faculty(name=fac_name,department=fac_dpt,gender=fac_gender,dob=fac_dob,email=fac_email,phone=fac_phone,password=fac_password)
        fac_obj.save()
    return render(request,'admins/faculty_register.html')




def profileA(request):
    return render(request,'admins/admin_profile.html')

def detailsSA(request):
    return render(request,'admins/admins_student_details.html')





def search_stu(request):
    if request.method == 'POST':
        dept = request.POST['dropdown1']
        sem = request.POST['dropdown2']
        print(sem)
        print(dept)

    student_data = Student.objects.filter(dpt=dept, semester=sem)
    return render(request,'admins/admins_student_details.html',{"stu_details":student_data})







def detailsFA(request):
    return render(request,'admins/admins_faculty_details.html')

def notificationsA(request):
    return render(request,'admins/admins_notifications.html')

def view(request):
    return render(request,'admins/view.html')