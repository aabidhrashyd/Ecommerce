from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=253)
    image = models.ImageField(upload_to="img")
    price = models.IntegerField()

def __str__(self):
    return self.name