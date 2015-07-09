from django.db import models
from decimal import Decimal

# Create your models here.
class Bottle(models.Model):
    classi = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    QOH = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    UOM = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)   
#    style1 = models.CharField(max_length=50)
#    style2 = models.CharField(max_length=50)
#    age = models.CharField(max_length=20)
#    brand = models.CharField(max_length=50)
#    origin = models.CharField(max_length=50)
#    region = models.CharField(max_length=50)
#    ABV = models.DecimalField(max_digits=4,decimal_places=1)
#    mytype = models.CharField(max_length=20)
#    category = models.CharField(max_length=50)
