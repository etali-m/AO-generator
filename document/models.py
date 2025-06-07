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

#Piece d'un Dossier d'appel d'offre
class Piece(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    nom_composant = models.CharField(max_length=100)
    type_marche = models.ForeignKey(TypeMarche, on_delete=models.CASCADE)
    statut = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.titre} - {self.type_marche.nom}'
    
#Appel d'offre 
class AppelOffre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_marche = models.ForeignKey(TypeMarche, on_delete=PROTECT)
    objet_appel = models.TextField()
    maitre_ouvrage = models.CharField(max_length=300)
    denomination = models.CharField(max_length=30)
    commission_marche = models.CharField(max_length=200)
    type_dossier = models.CharField(max_length=100)
    mode_passation = models.CharField(max_length=10)
    numero_dossier = models.IntegerField(blank=True, null=True)
    exercice_budgetaire = models.IntegerField()
    financement = models.CharField(max_length=300)
    imputation = models.CharField(max_length=200)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.objet_appel}'

    @property 
    def numero_appel_offre(self):
        lettre_type = self.type_dossier[0]
        lettre_passation = self.mode_passation[0]
        numero = (
            str(self.numero_dossier)
            + '/AO'
            + lettre_type
            + lettre_passation
            + '/'
            + self.denomination
            + '/'
            + self.commission_marche
            + '/'
            + str(self.exercice_budgetaire)
        )
        return numero.upper()


#Permet de créer stocker les instances de pièces d'un type de marché à chaque fois qu'on créé un dossier d'appel d'offre.
class StatutPiece(models.Model):
    appel_offre = models.ForeignKey(AppelOffre, on_delete=models.CASCADE, related_name='pieces')
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('appel_offre', 'piece')

    def __str__(self):
        return f"{self.piece.titre} ({self.appel_offre})"