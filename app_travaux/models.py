from django.db import models
from ckeditor.fields import RichTextField
from document.models import AppelOffre

# Create your models here.
class AvisAppelOffre(models.Model):
    appel_offre = models.ForeignKey(AppelOffre, on_delete=models.CASCADE)
    objet_appel = RichTextField()
    consistence_travaux = RichTextField()
    tranches = RichTextField()
    cout_previsionnel = RichTextField()
    delai_previsionnel = RichTextField()
    participation = RichTextField()
    financement = RichTextField()
    mode_soumission = models.CharField(max_length=100)
    caution_soumission = RichTextField()
    consultation_dossier = RichTextField()
    acquition_dao = RichTextField()
    remise_offre = RichTextField()
    recevabilite_plis = RichTextField()
    ouverture_plis = RichTextField()
    critere_eliminatoire = RichTextField()
    critere_essenetielles = RichTextField()
    attribution = RichTextField()
    nombre_max_lots = models.IntegerField()
    duree_validite = models.IntegerField()
    renseignement_complementaires = RichTextField()
    numero_moa = models.IntegerField()

    def __str__(self):
        return f"{self.appel_offre}"
