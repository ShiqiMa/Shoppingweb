from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True)
