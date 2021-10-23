from django.db import models

# Create your models here.
class Expert(models.Model):

    title = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='experts/')
    social_facebook = models.URLField(blank=True, null=True)
    social_github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Project(models.Model):

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    short_description = models.TextField()
    image = models.ImageField(upload_to='experts/')

    
    def __str__(self):
        return self.title

class Testimonial(models.Model):

    title = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    short_description = models.TextField()
    image = models.ImageField(upload_to='testimonial/')

    
    def __str__(self):
        return self.title