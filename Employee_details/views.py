from django import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from .forms import EmployeeForm
from .models import Employee




def Employee1(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            first_name = employee_form.cleaned_data['employee_firstname']
            last_name = employee_form.cleaned_data['employee_lastname']
            location = employee_form.cleaned_data['employee_location']
            salary = employee_form.cleaned_data['employee_salary']
            department = employee_form.cleaned_data['employee_department']
            reg = Employee(employee_firstname = first_name,employee_lastname = last_name,employee_location = location,
            employee_salary = salary,employee_department = department)
            reg.save()
            employee_form = EmployeeForm()
    else:
        employee_form = EmployeeForm()
    emp1 = Employee.objects.all()

    return render (request,"Employee_details/Employees.html",{
       "form" : employee_form,
       "emp" : emp1

    })

#This is for updating and edit the data


def update_data(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeForm(instance=pi)
    return render(request,"Employee_details/updateform.html",{
        "form" : fm
    })







#This function will delete

def delete_data(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")











