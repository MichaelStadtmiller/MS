from django.db import models
from decimal import Decimal

# Create your models here.
class Bottle(models.Model):
    PSID = models.IntegerField(primary_key=True)
    name = models.CharField(mex_lenght=100)
    img = models.CharField(mex_lenght=100)
    desc = models.CharField(mex_lenght=100)
    cat = models.CharField(mex_lenght=20)
    origin = models.CharField(mex_lenght=20)
    classi = models.CharField(max_length=50)   
    region = models.CharField(max_length=50)
    prodtype = models.CharField(max_length=50)
    ABV = models.DecimalField(max_digits=5,decimal_places=2)
    style1 = models.CharField(max_length=50)
    package = models.CharField(max_lenght=20)
    style2 = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    UOM = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    container = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    retail = models.DecimalField(max_digits=5,decimal_places=2)
    QOH = models.IntegerField(default=0)
    
