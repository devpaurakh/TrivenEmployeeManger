from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
class EmployeeInfo(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     empCode = models.CharField(max_length=50)
     empDepart = models.CharField(max_length=100,null=True)
     empDesignation = models.CharField(max_length=100,null=True)
     empGender = models.CharField(max_length=10,null=True)
     empContactNo = models.CharField(max_length=10,null=True)
     empJoiningdate = models.DateField(null=True)
     def __str__(self):
         return self.user.username



class EmployeeEducation(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     CorseMaster = models.CharField(max_length=100,null=True)
     schoolMaster = models.CharField(max_length=100,null=True)
     yearOfPassMaster = models.CharField(max_length=100,null=True)
     precentageMaster = models.CharField(max_length=100,null=True)
     

     CorseBachlor = models.CharField(max_length=100,null=True)
     schoolBachlor = models.CharField(max_length=100,null=True)
     yearOfPassBachlor = models.CharField(max_length=100,null=True)
     precentageBachlor = models.CharField(max_length=100,null=True)
     
     CorsePlus2 = models.CharField(max_length=100,null=True)
     schoolPlus2 = models.CharField(max_length=100,null=True)
     yearOfPassPlus2 = models.CharField(max_length=100,null=True)
     precentagePlus2 = models.CharField(max_length=100,null=True)
     
     CorseSEE = models.CharField(max_length=100,null=True)
     schoolSEE = models.CharField(max_length=100,null=True)
     yearOfPassSEE = models.CharField(max_length=100,null=True)
     precentageSEE = models.CharField(max_length=100,null=True)
     def __str__(self):
         return self.user.username
     
     
     
class EmployeeExp(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     CompanyOneName = models.CharField(max_length=100,null=True)
     CompanyOneDesig = models.CharField(max_length=100,null=True)
     CompanyOneSalary = models.CharField(max_length=100,null=True)
     CompanyOneDuration = models.CharField(max_length=100,null=True)
     

     CompanyTwoName = models.CharField(max_length=100,null=True)
     CompanyTwoDesig = models.CharField(max_length=100,null=True)
     CompanyTwoSalary = models.CharField(max_length=100,null=True)
     CompanyTwoDuration = models.CharField(max_length=100,null=True)
     
     CompanyThreeName = models.CharField(max_length=100,null=True)
     CompanyThreeDesig = models.CharField(max_length=100,null=True)
     CompanyThreeSalary = models.CharField(max_length=100,null=True)
     CompanyThreeDuration = models.CharField(max_length=100,null=True)
     def __str__(self):
         return self.user.username


