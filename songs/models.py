from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField()

class Song(models.Model):
    title = models.CharField(max_length=100)
    



