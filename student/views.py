from django.shortcuts import render,redirect
import faculty
from faculty.models import Student,FacultyAuthentication

# Create your views here.
def login_student(request):
    error=''
    if request.method=='POST':
        stu_email=request.POST['s_email']
        stu_password=request.POST['s_password']
        try:
            user_data=Student.objects.get(email=stu_email,password=stu_password)
            request.session['student_id']=user_data.id
            request.session['dep']=user_data.dpt
            request.session['sem']=user_data.semester
            return redirect('student:student_home')
        except:
            error="invalid username or password"

    return render(request,'student/student_login.html',{'error':error})








def forgotpwS(request):
    return render(request,'student/student_forgot_pw.html')  






def student_home(request):
    student_name= request.session['student_id']
    student_display=Student.objects.get(id=student_name)
    return render(request,'student/student_home.html',{'stu':student_display})  





def student_profile(request):
    student_name= request.session['student_id']
    student_display=Student.objects.get(id=student_name)
    return render(request,'student/student_profile.html',{'stu':student_display})     






def student_authentication(request):
    student_name= request.session['student_id']
    student_display=Student.objects.get(id=student_name)
    return render(request,'student/student_authentication.html',{'stu':student_display}) 










def student_msg(request):
    data=FacultyAuthentication.objects.filter(ac_sem=request.session['sem'],ac_dpt=request.session['dep'])
    print(data)
    return render(request,'student/student_msg.html',{'data':data,})  







def student_chat(request):
    return render(request,'student/student_chat.html')     

