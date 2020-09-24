from django.db import models

# Create your models here.

class Gowns(models.Model):
  
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()
    desc = models.TextField()
    offer = models.BooleanField(default = True)

