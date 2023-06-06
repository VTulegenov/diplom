from django.db import models
from departament.models import Departament


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    hire_data = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
