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
    liste_prequalifie =  RichTextField(blank=True, null=True)
    provenance_materiaux = RichTextField()
    renseignements_necessaires = RichTextField(blank=True, null=True)
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
    mode_soumission = RichTextField()
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

class CCAP(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE)
    chef_service_marche = models.CharField(max_length=100)
    ing_marche = models.CharField(max_length=100)
    control_externe = models.CharField(max_length=100)
    cocontractant = models.CharField(max_length=100, blank=True, null=True)
    autorite_ordonnancement = models.CharField(max_length=100)
    autorite_liquidation = models.CharField(max_length=100)
    organisme_paiment = models.CharField(max_length=100)
    responsable_renseignement = models.CharField(max_length=100)
    pieces_constitutive_marche = RichTextField()
    textes_applicables = RichTextField()
    communication = RichTextField()
    delai_execution = RichTextField()
    marche_a_tranche = RichTextField(blank=True, null=True)
    personnel_entreprise = RichTextField()
    replacement_personnel = RichTextField()
    programme_travaux = RichTextField()
    projet_execution = RichTextField()
    labo_chantier = RichTextField()
    reunion_chantier = RichTextField()
    utilisation_explosifs = RichTextField(blank=True, null=True)
    operation_prealable_reception = RichTextField()
    commission_reception = RichTextField()
    reception_partielle = RichTextField(blank=True, null=True)
    periode_garantie = RichTextField(blank=True, null=True)
    documente_a_fournir = RichTextField()
    delai_garantie = RichTextField()
    reception_definitive = RichTextField()
    cautionnement_definitif = RichTextField()
    cautionnement_garantie = RichTextField()
    cautionnement_avance_demarrage = RichTextField()
    variation_prix = RichTextField()
    revision_prix = RichTextField()
    actualisation_prix = RichTextField()
    travaux_regie = RichTextField()
    valorisation_approvisionnement = RichTextField()
    avances = RichTextField()
    decompte_provisoir = RichTextField()
    decompte_final = RichTextField()
    decompte_defintif = RichTextField()
    reglement_groupement = RichTextField(blank=True, null=True)
    regime_fiscal = RichTextField()
    resiliation_marche = RichTextField(blank=True, null=True)
    force_majeure = RichTextField()
    differends_litiges = RichTextField()
    edition_marche = RichTextField()
    entree_en_vigueur = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"


#Bordereau des prix unitaires
class BPU(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE)
    prix_unitaires = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"


#Devis quantitatif et estimatif
class DQE(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE)
    dqe = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"