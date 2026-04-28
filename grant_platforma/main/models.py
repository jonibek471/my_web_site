
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    gpa = models.FloatField()
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grant(models.Model):
    title = models.CharField(max_length=200)
    min_gpa = models.FloatField()
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.title