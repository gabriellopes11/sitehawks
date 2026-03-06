from django.db import models

class Player(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()
    posicao = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='players/')

class Sponsor(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/')
    site = models.URLField(blank=True)

    def __str__(self):
         return self.nome