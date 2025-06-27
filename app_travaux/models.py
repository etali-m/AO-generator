from django.db import models
from ckeditor.fields import RichTextField
from document.models import AppelOffre

# Create your models here.
class AvisAppelOffre(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE)
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
    acquisition_dao = RichTextField()
    remise_offre = RichTextField()
    recevabilite_plis = RichTextField()
    ouverture_plis = RichTextField()
    critere_eliminatoire = RichTextField()
    critere_essentielles = RichTextField()
    attribution = RichTextField()
    nombre_max_lots = models.IntegerField()
    duree_validite = models.IntegerField()
    renseignement_complementaires = RichTextField()
    numero_moa = models.IntegerField()

    def __str__(self):
        return f"{self.appel_offre}"


class RPAO(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE)
    consistenceTravaux =  RichTextField()
    liste_prequalifie =  RichTextField()
    provenance_materiaux = RichTextField()
    renseignements_necessaires = RichTextField()
    visite_travaux = RichTextField()
    renseignements_complementaires = RichTextField()
    langue_soumission = RichTextField()
    piecesAdminLocales = RichTextField()
    piecesAdminEtrangeres = RichTextField()
    refSoumissionnaire = RichTextField()
    personnel = RichTextField()
    materiels = RichTextField()
    organisation_methodologie = RichTextField()
    respect_formulaire = RichTextField()
    preuve_acceptation = RichTextField()
    commentaire_ccap = RichTextField()
    capacite_financiere = RichTextField()
    offreFinanciere = RichTextField()
    impots_taxes = RichTextField()
    prix_marche = RichTextField()
    monnaies_soumission = RichTextField()
    taux_change = RichTextField()
    validite_offre = RichTextField()
    montant_cautionnement = RichTextField()
    evaluation_offres = RichTextField()
    variante_techniques = RichTextField()
    reunion_preparatoire = RichTextField()
    soumission_en_ligne = RichTextField()
    date_heure_limite = RichTextField() 
    ouverture_plis = RichTextField()
    qualification_soumissionaire = RichTextField()
    criteres_eliminatoires = RichTextField()
    criteres_essentiels = RichTextField()
    monnaie_retenu = RichTextField()
    mode_evaluation = RichTextField()
    ref_32_2_e = RichTextField()
    ref_32_2_g = RichTextField()
    ref33_1 = RichTextField()
    ref_34_1 = RichTextField()
    ref_34_2 = RichTextField()
    ref_39_2 = RichTextField()
    ref_40 = RichTextField

    def __str__(self):
        return f"{self.appel_offre}"
