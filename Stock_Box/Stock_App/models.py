from django.db import models
import pandas as pd

# Create your models here.
# Django model fields (Plenty of documentation on this)
class ex_obj(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField
    
class stock(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    full_name= models.CharField(max_length=100)
