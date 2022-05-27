from django.http import HttpResponse
from django.shortcuts import render,redirect
from admins.models import Faculty
from faculty.models import Student
from faculty.models import FacultyAuthentication

# Create your views here.





def login_faculty(request):
    error=''
    if request.method=='POST':
        fac_email=request.POST['f_email']
        fac_password=request.POST['f_password']
        try:
            user_data=Faculty.objects.get(email=fac_email,password=fac_password)
            request.session['faculty_id']=user_data.id
            return redirect('faculty:faculty_home')
        except:
           error="invalid username or password"

    return render(request,'faculty/faculty_login.html',{'error':error})








def forgotpwF(request):
    return render(request,'faculty/faculty_forgot_pw.html')









def faculty_home(request):
    faculty_name=request.session['faculty_id']
    faculty_display=Faculty.objects.get(id=faculty_name)
    return render(request,'faculty/faculty_home.html',{'fac':faculty_display})








def faculty_profile(request):
    faculty_name=request.session['faculty_id']
    faculty_display=Faculty.objects.get(id=faculty_name)
    return render(request,'faculty/faculty_profile.html',{'fac':faculty_display})







def faculty_authentication(request):
    if request.method=="POST":
        current_user = request.session['faculty_id']
        user_obj = Faculty.objects.get(id=current_user)

        # current_display = FacultyAuthentication.objects.get(id=current_user)
        fac_ac_dpt=request.POST['ac_department']
        fac_ac_sem=request.POST['ac_semester']
        fac_ac_subject=request.POST['ac_sub']
        fac_ac_code=request.POST['ac_code']

        fac_ac_obj=FacultyAuthentication(ac_dpt=fac_ac_dpt,ac_sem=fac_ac_sem,ac_subject=fac_ac_subject,ac_authentication=fac_ac_code,faculty_id=user_obj)
        fac_ac_obj.save()
    return render(request,'faculty/faculty_authentication.html')







def student_register(request):
    if request.method=='POST':
        stu_name=request.POST['s_name']
        stu_eno=request.POST['s_eno']
        stu_dob=request.POST['s_dob']
        stu_gender=request.POST['s_gender'] 
        stu_dpt=request.POST['s_dpt'] 
        stu_sem=request.POST['s_sem']
        stu_email=request.POST['s_email']  
        stu_phone=request.POST['s_phone'] 
        stu_password=request.POST['s_password']

        stu_obj=Student(name=stu_name,eno=stu_eno,dob=stu_dob,gender=stu_gender,dpt=stu_dpt,semester=stu_sem,email=stu_email,phone=stu_phone,password=stu_password)
        stu_obj.save()
    return render(request,'faculty/student_register.html')






def student_details(request):
    return render(request,'faculty/student_details.html')







def search_student(request):
    if request.method == 'POST':
        dept = request.POST['dropdown1']
        sem = request.POST['dropdown2']
        print(sem)
        print(dept)

    student_data = Student.objects.filter(dpt=dept, semester=sem)
    return render(request,'faculty/student_details.html',{"stu_details":student_data})







    

def attendance_date(request):
    return render(request,'faculty/student_attendanceD.html')

def attendance_month(request):
    return render(request,'faculty/student_attendanceM.html')




# def faculty_msg(request):
#     faculty_name=request.session['faculty_id']
#     faculty_display=FacultyAuthentication.objects.get(id=faculty_name)
#     return render(request,'faculty/faculty_msg.html',{'fac':faculty_display})



def faculty_msg(request):
    return render(request,'faculty/faculty_msg_student.html')

def faculty_chat_student(request):
    return render(request,'faculty/faculty_chat_student.html')

def faculty_chat_admin(request):
    return render(request,'faculty/faculty_chat_admin.html')





