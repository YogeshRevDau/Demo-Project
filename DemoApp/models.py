from django.db import models

from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)  # Add a default quantity of 1
    price_individual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item = models.CharField(max_length=120)
