from django.db import models
from datetime import date


class Dog(models.Model):
    name = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    birthday = models.DateField(default=date.today)

    def __str__(self):
        return self.name
