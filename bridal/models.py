from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


# Create your models here.

class Gowns(models.Model):
    STATUS = (
        ('True', 'True' ),
        ('False', 'False'),
    )
  
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()
    desc = RichTextUploadingField()
    offer = models.BooleanField(default = True)

    def __str__(self):
        return self.name


class Page_inf(models.Model):
    STATUS = (
        ('True', 'True' ),
        ('False', 'False'),
    )
    title = models.CharField(blank=True,max_length=15)
    keywords = models.CharField(blank=True,max_length=15)
    description = models.CharField(blank=True,max_length=20)
    company = models.CharField(blank=True,max_length=15)
    address = models.CharField(blank=True,max_length=15)
    phone = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=15)
    facebook = models.CharField(blank=True,max_length=20)
    instagram = models.CharField(blank=True,max_length=20)
    twitter = models.CharField(blank=True,max_length=20)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    

    def __str__(self):
        return self.title


