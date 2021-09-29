from django.db import models

class Employee(models.Model):
    employee_firstname = models.CharField(max_length=50)
    employee_lastname = models.CharField(max_length=100)
    employee_location = models.CharField(max_length=150)
    employee_salary = models.IntegerField()
    employee_department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee_firstname}{self.employee_lastname}"










    