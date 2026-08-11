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
    renseignement_complementaires = RichTextField()

    # ===== Champs communs =====
    nombre_max_lots = models.IntegerField()
    duree_validite = models.IntegerField()
    numero_moa = models.IntegerField(blank=True, null=True)

    # ===== Spécifique conception-réalisation (concours) =====
    note_artistique_minimale = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # ===== Version anglaise (générée) =====
    objet_appel_en = RichTextField(blank=True, null=True)
    consistence_travaux_en = RichTextField(blank=True, null=True)
    tranches_en = RichTextField(blank=True, null=True)
    cout_previsionnel_en = RichTextField(blank=True, null=True)
    delai_previsionnel_en = RichTextField(blank=True, null=True)
    participation_en = RichTextField(blank=True, null=True)
    financement_en = RichTextField(blank=True, null=True)
    mode_soumission_en = models.CharField(max_length=100, blank=True, null=True)
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
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='rpao_cr')

    # ===== Réutilisés (même sens que le RPAO travaux) =====
    provenance_materiaux = RichTextField()
    visite_travaux = RichTextField()
    renseignements_necessaires = RichTextField(blank=True, null=True)
    renseignements_complementaires = RichTextField()
    langue_soumission = RichTextField()
    piecesAdminLocales = RichTextField()
    piecesAdminEtrangeres = RichTextField()
    refSoumissionnaire = RichTextField()
    personnel = RichTextField()
    materiels = RichTextField()
    organisation_methodologie = RichTextField()
    preuve_acceptation = RichTextField()
    commentaire_ccap = RichTextField()
    prix_marche = RichTextField()
    monnaies_soumission = RichTextField()
    taux_change = RichTextField()
    monnaie_retenu = RichTextField()
    validite_offre = RichTextField()
    montant_cautionnement = RichTextField()
    variante_techniques = RichTextField()
    reunion_preparatoire = RichTextField()
    soumission_en_ligne = RichTextField()
    mode_soumission = RichTextField()
    date_heure_limite = RichTextField()
    criteres_eliminatoires = RichTextField()
    criteres_essentiels = RichTextField()
    mode_evaluation = RichTextField()

    # ===== Spécifique conception-réalisation (concours bi-phase) =====
    descriptif_operation = RichTextField()
    lieu_execution = RichTextField()
    objectifs_mission = RichTextField()
    source_financement_rpao = RichTextField()
    delai_phase_conception = RichTextField()
    delai_phase_realisation = RichTextField()
    delai_global = RichTextField()
    cout_global_previsionnel = RichTextField()
    nombre_exemplaires_dossier_administratif = models.IntegerField(blank=True, null=True)
    nombre_exemplaires_proposition_artistique = models.IntegerField(blank=True, null=True)
    nombre_exemplaires_proposition_technique = models.IntegerField(blank=True, null=True)
    adresse_depot_offres = RichTextField()
    avant_projet_sommaire = RichTextField()
    liste_etudes_conception = RichTextField()
    cout_etudes = RichTextField()
    cout_estimatif_projet = RichTextField()
    cout_global_projet = RichTextField()
    formation_element_majeur = models.BooleanField(default=False)
    poids_artistique = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    poids_technique = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    poids_financiere = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    taux_cautionnement_definitif_rpao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

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
