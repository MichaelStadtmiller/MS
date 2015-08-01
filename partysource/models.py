from django.db import models

# Create your models here.
class Bottle(models.Model):
    PSID = models.IntegerField(null=True)
    name = models.CharField(max_length=100,default='')
    img = models.CharField(max_length=100,default='')
    desc = models.CharField(max_length=300,default='')
    cat = models.CharField(max_length=20,default='')
    origin = models.CharField(max_length=20,default='')
    classi = models.CharField(max_length=50,default='')
    region = models.CharField(max_length=50,default='')
    prodtype = models.CharField(max_length=50,default='')
    ABV = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    style1 = models.CharField(max_length=50,default='')
    package = models.CharField(max_length=20,default='')
    style2 = models.CharField(max_length=50,default='')
    size = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    UOM = models.CharField(max_length=10,default='')
    age = models.CharField(max_length=10,default='')
    container = models.CharField(max_length=20,default='')
    brand = models.CharField(max_length=50,default='')
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    retail = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    QOH = models.IntegerField(default=0)

    def __str__(self):
        return self.name    
