from django.db import models
from django.db.models.fields import CharField


# Create your models

class Corousel(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()

    image = models.ImageField(upload_to='carousel/')
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
