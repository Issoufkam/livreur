from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    numero = models.CharField(max_length=10)
    nom = models.CharField(max_length=255)