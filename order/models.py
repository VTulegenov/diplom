from django.db import models
from customer.models import Customer
from employee.models import Employee


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_data = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=8, decimal_places=2)

