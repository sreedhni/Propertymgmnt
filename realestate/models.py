

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11)
    address= models.CharField(max_length=128)

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    features = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.PositiveIntegerField()
    options = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    type = models.CharField(max_length=4, choices=options)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.property.name


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    document_proofs =models.ImageField(upload_to="images")

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name



class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE,related_name="tenant")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


