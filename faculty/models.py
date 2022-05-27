from django.db import models

from admins.models import Faculty

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    eno=models.BigIntegerField()
    dob=models.CharField(max_length=25)
    gender=models.CharField(max_length=20)
    dpt=models.CharField(max_length=20)
    semester=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=30)


    class Meta:
        db_table="student"






class FacultyAuthentication(models.Model):
    ac_dpt=models.CharField(max_length=20)
    ac_sem=models.CharField(max_length=20)
    ac_subject=models.CharField(max_length=20)
    ac_authentication=models.CharField(max_length=20)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)


    class Meta:
        db_table="authentication_fac"