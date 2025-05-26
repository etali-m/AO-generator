from django.db import models
from django.db.models import PROTECT
from autoslug import AutoSlugField
from account.models import User

# Create your models here.
class TypeMarche(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_garde = models.ImageField(upload_to='template_marche/')
    slug = AutoSlugField(unique=True, populate_from='nom')

    def __str__(self):
        return f'{self.nom}'

class Piece(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    nom_composant = models.CharField(max_length=100)
    type_marche = models.ForeignKey(TypeMarche, on_delete=models.CASCADE)
    
#Appel d'offre 
class AppelOffre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_marche = models.ForeignKey(TypeMarche, on_delete=PROTECT)
    objet_appel = models.TextField()
    maitre_ouvrage = models.CharField(max_length=300)
    denomination = models.CharField(max_length=30)
    commission_marche = models.CharField(max_length=200)
    type_dossier = models.CharField(max_length=100)
    numero_dossier = models.IntegerField(blank=True, null=True)
    exercice_budgetaire = models.IntegerField()
    financement = models.CharField(max_length=300)
    imputation = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.objet_appel}'