from django.db import models

# Create your models here.
from django.db import models
class Acteur(models.Model):
        nom = models.CharField(max_length=200)
        email=models.EmailField()
