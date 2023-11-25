from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def homepage(request):
    return render(request,'index.html')


#sign up for employee
def signup(request):
    showError=""
    if request.method == "POST":
        firstName = request.POST['firstname']
        lastName = request.POST['lname']
        code = request.POST['code']
        email = request.POST['email']
        passw = request.POST['pw']
        # Check if the email (username) already exists
        if User.objects.filter(username=email).exists():
            showError = "exists"
        else:
            try:
                users = User.objects.create_user(first_name=firstName, last_name=lastName, username=email, password=passw)
                EmployeeInfo.objects.create(user = users,empCode = code)
                EmployeeExp.objects.create(user = users)
                EmployeeEducation.objects.create(user = users)
                showError = "no"
            except Exception as e:
                    showError = "yes"
    return render(request,'registration.html',locals())


#login for employee in this function
def empLogin(request):
    showError=""
    if request.method == 'POST':
        loginEmail = request.POST['emailid']
        loginPassword = request.POST['password']
        loginedUser = authenticate(username = loginEmail, password = loginPassword)
        if loginedUser:
            login(request,loginedUser)
            showError = "no"
        else:
            showError = "yes"
    return render(request,'emp_login.html',locals())


def emp_home(request):
#for uservalidation is login or not
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

#logout off the system
def user_logout(request):
    logout(request)
    return redirect('index')


#employee data in the profile page
def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    showError=""
    user = request.user
    employee = EmployeeInfo.objects.get(user = user)
    #collect data from the profile page
    if request.method == "POST":
        firstName = request.POST['firstname']
        lastName = request.POST['lname']
        code = request.POST['code']
        designation = request.POST['emp_desig']
        department = request.POST['emp_department']
        contact = request.POST['contact']
        joining_date = request.POST['joinDate']
        gender = request.POST['gender']
        
        #now up datinng the value
        employee.user.first_name = firstName
        employee.user.last_name = lastName
        employee.empCode = code
        employee.empDesignation = designation
        employee.empDepart = department
        employee.empGender = gender
        employee.empContactNo = contact
        if joining_date:
            employee.empJoiningdate = joining_date
        
        try:
            employee.save()
            employee.user.save()
            showError = "no"
        except Exception as e:
                showError = "yes"
   
    return render(request,'emp_profile.html',locals())





def my_exp(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    Exp = EmployeeExp.objects.get(user = user)
    return render(request,'my_exp.html',locals())


def my_exp_edit(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    showError=""
    user = request.user
    Exp = EmployeeExp.objects.get(user = user)
    
    if request.method == "POST":
        CompanyOneName = request.POST['CompanyOneName']
        CompanyOneDesig = request.POST['CompanyOneDesig']
        CompanyOneSalary = request.POST['CompanyOneSalary']
        CompanyOneDuration = request.POST['CompanyOneDuration']
        
        CompanyTwoName = request.POST['CompanyTwoName']
        CompanyTwoDesig = request.POST['CompanyTwoDesig']
        CompanyTwoSalary = request.POST['CompanyTwoSalary']
        CompanyTwoDuration = request.POST['CompanyTwoDuration']
        
        CompanyThreeName = request.POST['CompanyThreeName']
        CompanyThreeDesig = request.POST['CompanyThreeDesig']
        CompanyThreeSalary = request.POST['CompanyThreeSalary']
        CompanyThreeDuration = request.POST['CompanyThreeDuration']

        #now up datinng the value
        # values are like exp.inputField name = local variable name in request.menthod == 'POST'
        Exp.CompanyOneName = CompanyOneName
        Exp.CompanyOneDesig = CompanyOneDesig
        Exp.CompanyOneSalary = CompanyOneSalary
        Exp.CompanyOneDuration = CompanyOneDuration
        
        Exp.CompanyTwoName = CompanyTwoName
        Exp.CompanyTwoDesig = CompanyTwoDesig
        Exp.CompanyTwoSalary = CompanyTwoSalary
        Exp.CompanyTwoDuration = CompanyTwoDuration
        
        Exp.CompanyThreeName = CompanyThreeName
        Exp.CompanyThreeDesig = CompanyThreeDesig
        Exp.CompanyThreeSalary = CompanyThreeSalary
        Exp.CompanyThreeDuration = CompanyThreeDuration
        try:
            Exp.save()
            showError = "no"
        except Exception as e:
                showError = "yes"
   
    return render(request,'editExperienceDetail.html',locals())

# This is for the model f

def my_edu(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    Edu = EmployeeEducation.objects.get(user = user)
    return render(request,'emp_education.html',locals())


def my_edu_edit(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    showError=""
    user = request.user
    Edu = EmployeeEducation.objects.get(user = user)
    
    if request.method == "POST":
        CorseMaster = request.POST['CorseMaster']
        schoolMaster = request.POST['schoolMaster']
        yearOfPassMaster = request.POST['yearOfPassMaster']
        precentageMaster = request.POST['precentageMaster']
        
        CorseBachlor = request.POST['CorseBachlor']
        schoolBachlor = request.POST['schoolBachlor']
        yearOfPassBachlor = request.POST['yearOfPassBachlor']
        precentageBachlor = request.POST['precentageBachlor']
        
        CorsePlus2 = request.POST['CorsePlus2']
        schoolPlus2 = request.POST['schoolPlus2']
        yearOfPassPlus2 = request.POST['yearOfPassPlus2']
        precentagePlus2 = request.POST['precentagePlus2']
        
        CorseSEE = request.POST['CorseSEE']
        schoolSEE = request.POST['schoolSEE']
        yearOfPassSEE = request.POST['yearOfPassSEE']
        precentageSEE = request.POST['precentageSEE']

        #now up datinng the value
        # values are like edu.inputField name = local variable name in request.menthod == 'POST'
        Edu.CorseMaster = CorseMaster
        Edu.schoolMaster = schoolMaster
        Edu.yearOfPassMaster = yearOfPassMaster
        Edu.precentageMaster = precentageMaster
        
        Edu.CorseBachlor = CorseBachlor
        Edu.schoolBachlor = schoolBachlor
        Edu.yearOfPassBachlor = yearOfPassBachlor
        Edu.precentageBachlor = precentageBachlor
        
        Edu.CorsePlus2 = CorsePlus2
        Edu.schoolPlus2 = schoolPlus2
        Edu.yearOfPassPlus2 = yearOfPassPlus2
        Edu.precentagePlus2 = precentagePlus2
        
        Edu.CorseSEE = CorseSEE
        Edu.schoolSEE = schoolSEE
        Edu.yearOfPassSEE = yearOfPassSEE
        Edu.precentageSEE = precentageSEE
        try:
            Edu.save()
            showError = "no"
        except Exception as e:
                showError = "yes"
    return render(request,'editEducation.html',locals())



#change Password

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    showError=""
    user = request.user
    if request.method == "POST":
        current_password = request.POST['currentpassword']
        new_password = request.POST['new_password']
        try:
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                showError = "no"
            else:
                showError = "not"
        except Exception as e:
                showError = "yes"
    return render(request,'change_password_employee.html',locals())




def admin_dashboard(request):
#for uservalidation is login or not
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_dashboard.html')


def admin_login(request):
#for uservalidation is login or not
    showError=""
    if request.method == 'POST':
        uName = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = uName, password = password)
        try: 
           if user.is_staff:
            login(request,user)
            showError = "no"
           else:
            showError = "yes"
        except:
          showError = "yes"
    return render(request,'admin_login.html',locals())



def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    showError=""
    user = request.user
    if request.method == "POST":
        current_password = request.POST['currentpassword']
        new_password = request.POST['new_password']
        try:
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                showError = "no"
            else:
                showError = "not"
        except Exception as e:
                showError = "yes"
    return render(request,'admin_change_password.html',locals())


def all_employee(request):
#for uservalidation is login or not
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeInfo.objects.all()
    return render(request,'all_employee.html',locals())


def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect(all_employee)

def edit_profile_admin(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    showError = ""
    employee = EmployeeInfo.objects.get(id = pid)
    if request.method == "POST":
        firstName = request.POST['firstname']
        lastName = request.POST['lname']
        code = request.POST['code']
        designation = request.POST['emp_desig']
        department = request.POST['emp_department']
        contact = request.POST['contact']
        joining_date = request.POST['joinDate']
        gender = request.POST['gender']
        
         #now up datinng the value
        employee.user.first_name = firstName
        employee.user.last_name = lastName
        employee.empCode = code
        employee.empDesignation = designation
        employee.empDepart = department
        employee.empGender = gender
        employee.empContactNo = contact
        if joining_date:
            employee.empJoiningdate = joining_date
        
        try:
            employee.save()
            employee.user.save()
            showError = "no"
        except:
            showError = "yes"
    return render(request,'edit_profile_admin.html',locals())
        

def edit_education_admin(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    showError=""
    user = User.objects.get(id = pid)
    Edu = EmployeeEducation.objects.get(user = user)
    
    if request.method == "POST":
        CorseMaster = request.POST['CorseMaster']
        schoolMaster = request.POST['schoolMaster']
        yearOfPassMaster = request.POST['yearOfPassMaster']
        precentageMaster = request.POST['precentageMaster']
        
        CorseBachlor = request.POST['CorseBachlor']
        schoolBachlor = request.POST['schoolBachlor']
        yearOfPassBachlor = request.POST['yearOfPassBachlor']
        precentageBachlor = request.POST['precentageBachlor']
        
        CorsePlus2 = request.POST['CorsePlus2']
        schoolPlus2 = request.POST['schoolPlus2']
        yearOfPassPlus2 = request.POST['yearOfPassPlus2']
        precentagePlus2 = request.POST['precentagePlus2']
        
        CorseSEE = request.POST['CorseSEE']
        schoolSEE = request.POST['schoolSEE']
        yearOfPassSEE = request.POST['yearOfPassSEE']
        precentageSEE = request.POST['precentageSEE']

        #now up datinng the value
        # values are like edu.inputField name = local variable name in request.menthod == 'POST'
        Edu.CorseMaster = CorseMaster
        Edu.schoolMaster = schoolMaster
        Edu.yearOfPassMaster = yearOfPassMaster
        Edu.precentageMaster = precentageMaster
        
        Edu.CorseBachlor = CorseBachlor
        Edu.schoolBachlor = schoolBachlor
        Edu.yearOfPassBachlor = yearOfPassBachlor
        Edu.precentageBachlor = precentageBachlor
        
        Edu.CorsePlus2 = CorsePlus2
        Edu.schoolPlus2 = schoolPlus2
        Edu.yearOfPassPlus2 = yearOfPassPlus2
        Edu.precentagePlus2 = precentagePlus2
        
        Edu.CorseSEE = CorseSEE
        Edu.schoolSEE = schoolSEE
        Edu.yearOfPassSEE = yearOfPassSEE
        Edu.precentageSEE = precentageSEE
        try:
            Edu.save()
            showError = "no"
        except Exception as e:
                showError = "yes"
    return render(request,'edit_education_admin.html',locals())



def edit_experience_admin(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    showError=""
    user = User.objects.get(id = pid)
    Exp = EmployeeExp.objects.get(user = user)
    
    if request.method == "POST":
        CompanyOneName = request.POST['CompanyOneName']
        CompanyOneDesig = request.POST['CompanyOneDesig']
        CompanyOneSalary = request.POST['CompanyOneSalary']
        CompanyOneDuration = request.POST['CompanyOneDuration']
        
        CompanyTwoName = request.POST['CompanyTwoName']
        CompanyTwoDesig = request.POST['CompanyTwoDesig']
        CompanyTwoSalary = request.POST['CompanyTwoSalary']
        CompanyTwoDuration = request.POST['CompanyTwoDuration']
        
        CompanyThreeName = request.POST['CompanyThreeName']
        CompanyThreeDesig = request.POST['CompanyThreeDesig']
        CompanyThreeSalary = request.POST['CompanyThreeSalary']
        CompanyThreeDuration = request.POST['CompanyThreeDuration']

        #now up datinng the value
        # values are like exp.inputField name = local variable name in request.menthod == 'POST'
        Exp.CompanyOneName = CompanyOneName
        Exp.CompanyOneDesig = CompanyOneDesig
        Exp.CompanyOneSalary = CompanyOneSalary
        Exp.CompanyOneDuration = CompanyOneDuration
        
        Exp.CompanyTwoName = CompanyTwoName
        Exp.CompanyTwoDesig = CompanyTwoDesig
        Exp.CompanyTwoSalary = CompanyTwoSalary
        Exp.CompanyTwoDuration = CompanyTwoDuration
        
        Exp.CompanyThreeName = CompanyThreeName
        Exp.CompanyThreeDesig = CompanyThreeDesig
        Exp.CompanyThreeSalary = CompanyThreeSalary
        Exp.CompanyThreeDuration = CompanyThreeDuration
        try:
            Exp.save()
            showError = "no"
        except Exception as e:
                showError = "yes"
   
    return render(request,'edit_experience_admin.html',locals())

    