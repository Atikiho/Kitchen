from django.contrib.auth import get_user_model
from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        to="DishType",
        related_name="dishes",
        on_delete=models.DO_NOTHING
    )
    cooks = models.ManyToManyField(to=get_user_model(), related_name="dishes")

    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
