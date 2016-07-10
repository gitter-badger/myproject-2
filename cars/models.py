from django.db import models


# Create your models here.

class CarMake(models.Model):
    make = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.make


class CarModel(models.Model):
    make = models.ForeignKey('cars.CarMake', related_name='car_make')
    model = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.model
