from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()

