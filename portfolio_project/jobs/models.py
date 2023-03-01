from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Job(models.Model):
    #image
    image = models.ImageField(upload_to ='images/')

    #summary

    summary = models.CharField(max_length=200)

    website= models.URLField(max_length=250)


    def __str__(self):
        return self.summary