from django.db import models

class blogs(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
