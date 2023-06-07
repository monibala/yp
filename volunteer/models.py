from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class volunteer_info(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    designation = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quote = RichTextField()
    address = models.TextField(blank=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(blank=True)
    fb_link = models.URLField(max_length=200,null=True)
    ln_link = models.URLField(max_length=200,null=True)
    tw_link = models.URLField(max_length=200,null=True)
    ins_link =models.URLField(max_length=200,null=True) 
    def __str__(self):
        return self.name
class become_volunteer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    mobile = models.IntegerField(blank=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=200)
    country =models.CharField(max_length=100)
    zipcode = models.IntegerField(blank=True)
    def __str__(self):
        return f'{(self.firstname)(self.lastname)}'