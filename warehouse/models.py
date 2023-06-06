from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
