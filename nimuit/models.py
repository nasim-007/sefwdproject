from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

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

class Service(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='services/')

    
    def __str__(self):
        return self.title

class Partner(models.Model):

    
    image = models.ImageField(upload_to='partner/')
    image_hover = models.ImageField(upload_to='partner/', blank=True)
    
    

class Award(models.Model):

    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='award/')

    
    def __str__(self):
        return self.title

class Appointment(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name