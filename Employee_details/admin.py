from Employee_details.views import Employee1
from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_firstname','employee_lastname',
    'employee_location','employee_salary','employee_department']