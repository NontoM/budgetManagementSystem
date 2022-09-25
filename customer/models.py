from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=11,decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=11,decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=11,decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=11,decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name