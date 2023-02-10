from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName=models.CharField(max_length=50)
    price=models.CharField(max_length=50)

    def __str__(self) :
        return self.ProductName
        