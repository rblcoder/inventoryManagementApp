from django.db import models

from products.models import Product, Currency, QuantityUnit


# Create your models here.

class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"

    city = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    total_value = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class PurchaseLineItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)
    quantityUnit = models.ForeignKey(Address, on_delete=models.PROTECT)

    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    total_value = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name + " " + self.quantity


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    total_value = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)


class SaleLineItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)
    quantityUnit = models.ForeignKey(QuantityUnit, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)
    total_value = models.FloatField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name + " " + self.quantity
