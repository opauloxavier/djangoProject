from django.db import models
from django import forms

class User(models.Model):

    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.email

class Genero(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Artista(models.Model):
    name = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Musica(models.Model):
    name = models.CharField(max_length=20)
    album = models.CharField(max_length=20)
    artist = models.CharField(max_length=20)

    def __str__(self):
        return self.name

