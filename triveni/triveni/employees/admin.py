from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(EmployeeInfo) #basic info of employee
admin.site.register(EmployeeEducation) #employee education
admin.site.register(EmployeeExp) #employee education

