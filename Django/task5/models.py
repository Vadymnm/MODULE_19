from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    age = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updater_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
