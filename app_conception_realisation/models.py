from django.db import models
from ckeditor.fields import RichTextField
from document.models import AppelOffre


class AvisAppelOffre(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='avisappeloffre_cr')

    # ===== Version française =====
    objet_appel = RichTextField()
    consistence_travaux = RichTextField()
    tranches = RichTextField()
    cout_previsionnel = RichTextField()
    delai_previsionnel = RichTextField()
    participation = RichTextField()
    financement = RichTextField()
    mode_soumission = RichTextField()
    caution_soumission = RichTextField()
    consultation_dossier = RichTextField()
    acquisition_dao = RichTextField()
    remise_offre = RichTextField()
    recevabilite_plis = RichTextField()
    ouverture_plis = RichTextField()
    critere_eliminatoire = RichTextField()
    critere_essentielles = RichTextField()
    attribution = RichTextField()
    renseignement_complementaires = RichTextField()

    # ===== Champs communs =====
    
    duree_validite = models.IntegerField()
    numero_moa = models.IntegerField(blank=True, null=True)
    nombre_max_lots = models.IntegerField()
    #à supprimer
    
    note_artistique_minimale = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # ===== Version anglaise (générée) =====
    objet_appel_en = RichTextField(blank=True, null=True)
    consistence_travaux_en = RichTextField(blank=True, null=True)
    tranches_en = RichTextField(blank=True, null=True)
    cout_previsionnel_en = RichTextField(blank=True, null=True)
    delai_previsionnel_en = RichTextField(blank=True, null=True)
    participation_en = RichTextField(blank=True, null=True)
    financement_en = RichTextField(blank=True, null=True)
    mode_soumission_en = RichTextField(blank=True, null=True)
    caution_soumission_en = RichTextField(blank=True, null=True)
    consultation_dossier_en = RichTextField(blank=True, null=True)
    acquisition_dao_en = RichTextField(blank=True, null=True)
    remise_offre_en = RichTextField(blank=True, null=True)
    recevabilite_plis_en = RichTextField(blank=True, null=True)
    ouverture_plis_en = RichTextField(blank=True, null=True)
    critere_eliminatoire_en = RichTextField(blank=True, null=True)
    critere_essentielles_en = RichTextField(blank=True, null=True)
    attribution_en = RichTextField(blank=True, null=True)
    renseignement_complementaires_en = RichTextField(blank=True, null=True)

    # ===== Traçabilité de la traduction =====
    translated_at = models.DateTimeField(blank=True, null=True)
    valide_en = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.appel_offre}"


class RPAO(models.Model):
    """
    Les champs ref_X_Y correspondent directement aux références de la colonne
    "Références RGAO" du tableau du Règlement Particulier de l'Appel d'Offres
    conception-réalisation (DTAO ARMP, pages 58 à 86) : ref_1_1 = ligne "1.1"
    du tableau, ref_1_2 = ligne "1.2", etc. ref_17 correspond à la ligne sur la
    monnaie/taux de change dont le numéro était illisible dans le document
    source (imprimé "SI").
    """
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='rpao_cr')

    # ===== A. Généralités =====
    ref_1_1 = RichTextField(default='')   # Descriptif de l'opération
    ref_1_2 = RichTextField(default='')   # Étendue de la consultation (concours, mode de sélection, coût et délai globaux)
    ref_1_4 = RichTextField(default='')   # Répartition en phase conception et phase travaux
    ref_1_5 = RichTextField(default='')   # Conférence préalable à l'établissement des offres
    ref_1_6 = RichTextField(default='')   # Responsable(s) du Maître d'Ouvrage à contacter
    ref_2 = RichTextField(default='')     # Source(s) de financement

    # ===== B. Candidats admis à participer =====
    ref_4_2 = RichTextField(default='')   # Candidats admis à participer (groupement)
    ref_5_1 = RichTextField(default='')   # Provenance des matériaux, matériels et fournitures
    ref_6_2 = RichTextField(default='')   # Pièces à produire uniquement par le mandataire du groupement
    ref_7 = RichTextField(default='')     # Visite du site
    ref_9 = RichTextField(default='')     # Éclaircissements / renseignements complémentaires
    ref_11 = RichTextField(default='')    # Délai de dépôt des offres

    # ===== C. Préparation des offres =====
    ref_13_2 = RichTextField(default='')  # Volumes de soumission (4 enveloppes)
    ref_13_3 = RichTextField(default='')  # Soumission électronique
    ref_13_4 = RichTextField(default='')  # Lieu, date et heure limite de dépôt
    ref_13_7 = RichTextField(default='')  # Ouverture des plis (2 temps)
    ref_14 = RichTextField(default='')    # Langue de l'offre et volumes attendus

    # ===== D. Offre financière et prix =====
    ref_15_1 = RichTextField(default='')  # Caution de soumission et dossier administratif détaillé
    ref_16_1 = RichTextField(default='')  # Montant de l'offre / coût global du projet
    ref_16_4 = RichTextField(default='')  # Variation des prix
    ref_17 = RichTextField(default='')    # Monnaie de soumission et taux de change

    # ===== E. Validité, cautionnement, variantes, mode de soumission =====
    ref_18 = RichTextField(default='')    # Délai de validité des offres
    ref_19 = RichTextField(default='')    # Montant de la caution de soumission
    ref_20_3 = RichTextField(default='')  # Variantes
    ref_22_5 = RichTextField(default='')  # Mode de soumission (en ligne / hors ligne)

    # ===== F. Évaluation =====
    ref_24 = RichTextField(default='')    # Critères d'évaluation (éliminatoires et essentiels)
    criteres_eliminatoires = RichTextField(default='')  # Détail des critères éliminatoires (référence 24)
    criteres_essentiels = RichTextField(default='')     # Détail des critères essentiels (référence 24)
    ref_25 = RichTextField(default='')    # Grille détaillée des critères et sous-critères (NA, NT, NF, NG)

    # ===== G. Attribution et éthique =====
    ref_30 = RichTextField(default='')    # Cautionnement définitif
    ref_35 = RichTextField(default='')    # Attribution du marché
    ref_36 = RichTextField(default='')    # Principes éthiques

    # ===== Champs structurés dérivés (réutilisés ailleurs dans l'application) =====
    formation_element_majeur = models.BooleanField(default=False)
    poids_artistique = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    poids_technique = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    poids_financiere = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.appel_offre}"


# Grille de notation du concours (pièce 3 - saisie ; pièce 16 - restitution en lecture seule)
class GrilleNotation(models.Model):
    appel_offre = models.ForeignKey(AppelOffre, on_delete=models.CASCADE, related_name='grille_notation_cr')

    CATEGORIE_CHOICES = (
        ('artistique', 'Proposition artistique'),
        ('technique', 'Proposition technique'),
        ('financiere', 'Proposition financière'),
    )

    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    critere = models.CharField(max_length=255)
    sous_critere = models.CharField(max_length=255, blank=True, null=True)
    points = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.appel_offre} - {self.critere}"


class CCAP(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='ccap_cr')

    # ===== Réutilisés (identiques au CCAP travaux) =====
    chef_service_marche = models.CharField(max_length=100)
    contractant = models.CharField(max_length=100)
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

    # ===== Spécifique conception-réalisation (double intervenant / double phase) =====
    maitrise_oeuvre_conception = RichTextField()
    maitre_oeuvre_realisation = RichTextField()
    assistant_maitrise_ouvrage = RichTextField(blank=True, null=True)
    consistance_phase_conception = RichTextField()
    consistance_phase_realisation = RichTextField()
    montant_phase1 = RichTextField()
    montant_phase2 = RichTextField()
    commission_suivi_recette_conception = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"


# Termes de référence (pièce 5 - sans équivalent côté travaux)
class TDR(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='tdr_cr')
    contexte_justification = RichTextField()
    objectif_conception = RichTextField()
    resultats_attendus = RichTextField()
    qualification_consultants = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"


class CCTP(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='cctp_cr')
    clauses_techniques = RichTextField()

    def __str__(self):
        return f"{self.appel_offre}"


class BPU_DQE(models.Model):
    appel_offre = models.ForeignKey(AppelOffre, on_delete=models.CASCADE, related_name='bpu_dqe_cr')

    type = models.CharField(max_length=20)
    title = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)


class ModelMarche(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='modelmarche_cr')
    region = models.CharField(max_length=100, blank=True, null=True)
    departement = models.CharField(max_length=100, blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='logo_moa', blank=True, null=True)

    def __str__(self):
        return f"{self.appel_offre}"


# Justificatifs des études préalables (pièce 17 - formulaire, contrairement à son
# équivalent "visa de maturité" côté travaux qui est une simple annexe statique)
class EtudePrealable(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='etude_prealable_cr')
    etude_prealable_date = models.DateField(blank=True, null=True)
    etude_prealable_maitre_oeuvre = models.CharField(max_length=255, blank=True, null=True)
    etude_prealable_references_marche = models.CharField(max_length=255, blank=True, null=True)
    etude_prealable_type = models.CharField(max_length=100, blank=True, null=True)
    etude_prealable_description = RichTextField(blank=True, null=True)
    etude_prealable_fichier = models.FileField(upload_to='etudes_prealables', blank=True, null=True)

    def __str__(self):
        return f"{self.appel_offre}"
