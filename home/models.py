from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class teams(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)


def __str__(self):
    return self.name

class event_info(models.Model):
    event_name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    loacation = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    cost = models.IntegerField(blank=True)
    website = models.URLField(max_length=200,blank=True)
    mobile = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.event_name
class contact_info(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

class campaign_mgmt(models.Model):
    image = models.ImageField(blank=True)
    desc = models.TextField(blank=True)
    key_factor = RichTextField()
class gallery_info(models.Model):
    image = models.ImageField(blank=True)
