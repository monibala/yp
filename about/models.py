from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class about_us(models.Model):
    description = RichTextField()
    who_We_are = RichTextField()
    what_we_do = RichTextField()
    why_choose =RichTextField()
    mission = RichTextField()
    def __str__(self):
        return self.description