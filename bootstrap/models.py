from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models

class Corousel(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()

    image = models.ImageField(upload_to='carousel/')
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_delete_url(self):
        return reverse("bootstrap:delete", kwargs={
            "id": self.id
            })

    def get_update_url(self):
        return reverse("bootstrap:update", kwargs={
            "id": self.id
            })