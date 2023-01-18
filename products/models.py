from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    name = models.TextField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(max_length=3500)

class siteimage(models.Model):
    image = models.ImageField(max_length=3500)
    name = models.TextField(max_length=100)   

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)  
    date_added = models.DateTimeField(auto_now=True)
    total = models.IntegerField(default=1)
    new_id = models.IntegerField()