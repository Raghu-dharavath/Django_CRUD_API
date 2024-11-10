from django.db import models

# Create your models here.

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name