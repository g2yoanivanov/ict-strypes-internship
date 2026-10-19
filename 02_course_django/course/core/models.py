"""
Models for the core app.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Car(models.Model):
    """
    Car model.
    """
    FUEL_TYPES = [
        ('D', 'Diesel'),
        ('G', 'Gas'),
        ('P', 'Petrol'),
        ('H', 'Hybrid'),
        ('E', 'Electric')
    ]

    brand = models.CharField(max_length=64)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2026),
        ]
    )
    power = models.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(1500)
        ]
    )
    fuel_type = models.CharField(
        max_length=1,
        choices=FUEL_TYPES
    )

    def __str__(self):
        return self.brand
    
