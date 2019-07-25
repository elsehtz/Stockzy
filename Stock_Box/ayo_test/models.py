from django.db import models

# Create your models here.
 
class shop_item:
    id: int
    name: str
    img: str
    desc: str
    price: int
class MySimpleModel(models.Model):
    col = models.CharField(max_length=10)