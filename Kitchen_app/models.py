from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        to="DishType",
        related_name="dishes",
        on_delete=models.DO_NOTHING
    )
    cooks = models.ManyToManyField(to="Cook", related_name="dishes")

    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
