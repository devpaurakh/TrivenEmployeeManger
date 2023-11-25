"""
URL configuration for triveni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="index"),
    path('home/',homepage, name="homepage"),
    path('Signup/',signup,name="signup"),
    path('emp_login/',empLogin,name="emp_login"),
    path('emp_home/',emp_home,name="emp_home"),
    path('emp_profile/',emp_profile,name="emp_profile"),
    path('admin_login/',admin_login,name="admin_login"),
    path('logout/',user_logout,name="logout"),
    path('my_exp/',my_exp,name="my_exp"),
    path('my_exp_deit/',my_exp_edit,name="my_exp_edit"),
    path('my_edu/',my_edu,name="my_edu"),
    path('my_edu_edit/',my_edu_edit,name="my_edu_edit"),
    path('change_password/',change_password,name="change_password"),
    path('admin_dashboard/',admin_dashboard,name="admin_dashboard"),
    path('admin_change_password/',admin_change_password,name="admin_change_password"), 
    path('all_employee/',all_employee,name="all_employee"),
    path('delete_employee/<int:pid>/',delete_employee, name='delete_employee'),
    path('edit_profile_admin/<int:pid>',edit_profile_admin,name="edit_profile_admin"),
    path('edit_education_admin/<int:pid>',edit_education_admin,name="edit_education_admin"),
    path('edit_experience_admin/<int:pid>',edit_experience_admin,name="edit_experience_admin"), 
]
