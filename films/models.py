from django.utils import timezone
from django.db import models

class Categorie(models.Model):
    nom=models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Film(models.Model):
    # REMPLACE 'Titre' PAR 'title' ICI :
    title = models.CharField(max_length=200) 
    date_sortie = models.IntegerField()
    qte_stock = models.IntegerField()
    prix_location = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)

    def nomCategorie(self):
        return self.categorie.nom