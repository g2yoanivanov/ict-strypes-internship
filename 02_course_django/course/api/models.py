from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    