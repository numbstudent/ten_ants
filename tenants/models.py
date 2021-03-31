from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Units(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    code = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100)
    base_price = models.BigIntegerField()
    base_stock = models.IntegerField()
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Stocks(models.Model):
    amount = models.IntegerField()
    price = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoices(models.Model):
    no = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="employee")
    customers = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="customer")
    total = models.BigIntegerField()


class Discount(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    amount = models.BigIntegerField()


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    invoice = models.ForeignKey(Invoices, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    price = models.BigIntegerField()
    subtotal = models.BigIntegerField()
    discount_custom = models.BigIntegerField()
    discount_listed = models.BigIntegerField()
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
