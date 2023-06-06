from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
