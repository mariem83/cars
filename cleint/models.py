from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __init__(self, name, location):
        self.name = name
        self.location = location




class Car(models.Model):
    model_name = models.CharField(max_length=100)
    model_year = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __init__(self, model_name, model_year, manufacturer):
        self.model_name = model_name
        self.model_year = model_year
        self.manufacturer = manufacturer



class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100, null=True)
    cars_owned = models.ManyToManyField(Car)

    def __init__(self, name, age, email, cars_owned):
        self.name = name
        self.age = age
        self.email = email
        self.cars_owned = cars_owned
from django.db import models

# Create your models here.
