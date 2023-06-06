from django.db import models
from customer.models import Customer


class BankAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
