from django import forms
from django.db.models.base import Model
from django.forms import fields, models
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
   
# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         Model =  Employee
#         fields = [ 'employee_firstname', 'employee_lastname','employee_location','employee_salary','employee_department']


    # employee_firstname = forms.CharField(label="First name", max_length=100)
    # employee_lastname = forms.CharField(label ="Last name",max_length=100)
    # employee_location = forms.CharField(label="location", max_length=150)
    # employee_salary = forms.IntegerField(label="salary")
    # employee_department = forms.CharField(label= "department", max_length=50)
