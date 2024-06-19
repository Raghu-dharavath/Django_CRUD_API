from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=50)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

class Mobile(models.Model):
    name = models.CharField(max_length=20)
    model = models.IntegerField()
    price = models.IntegerField()
    version = models.FloatField()    