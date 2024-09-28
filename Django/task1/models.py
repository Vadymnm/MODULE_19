from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.CharField(max_length=3)


    def __init__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(to=Buyer)


    def __init__(self):
        return self.title