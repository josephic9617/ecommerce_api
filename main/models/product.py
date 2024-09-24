from django.db import models
from main.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    made_in = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
