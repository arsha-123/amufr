from django.db import models

# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    gender=models.CharField(max_length=30)
    dob=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=40)

    class Meta:
        db_table="faculty"







class Admin(models.Model):
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="admin"
