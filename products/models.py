from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class QuantityUnit(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Inventories"
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)
    quantityUnit = models.ForeignKey(QuantityUnit, on_delete=models.PROTECT, related_name="quantity_unit")
    reorderLevel = models.FloatField(default=0)
    reorderQuantityUnit = models.ForeignKey(QuantityUnit, on_delete=models.PROTECT,
                                            related_name="reorder_quantity_unit")
    lastModifiedDate = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.product.name + " " + self.quantity


class Currency(models.Model):
    class Meta:
        verbose_name_plural = "Currencies"
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    lastModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
