from django.db import models
from django.contrib.auth.models import AbstractUser

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.license_plate

class Officer(AbstractUser):
    identification_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Officer'
        verbose_name_plural = 'Officers'