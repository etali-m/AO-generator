from django.db import models
from ckeditor.fields import RichTextField
from document.models import AppelOffre


class AvisAppelOffre(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='avisappeloffre_snq')

    # ===== Version française =====
    objet_appel = RichTextField()
    consistence_prestations = RichTextField()
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

    # ===== Version anglaise (générée) =====
    objet_appel_en = RichTextField(blank=True, null=True)
    consistence_prestations_en = RichTextField(blank=True, null=True)
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
    Les champs ref_X_Y correspondent aux références de la colonne "Références du
    RGAO" du tableau du Règlement Particulier de l'Appel d'Offres - Services non
    quantifiables et prestations intellectuelles (DTAO ARMP, pages 62 à 84).
    ref_1_1 = ligne "1.1" du tableau, ref_1_3 = ligne "1.3", etc.
    """
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='rpao_snq')

    # ===== A. Généralités =====
    ref_1_1 = RichTextField(default='')   # Référence de l'AO, nombre de lots, définition des prestations, mode de sélection
    ref_1_3 = RichTextField(default='')   # Délai prévisionnel d'exécution des prestations
    ref_1_4 = RichTextField(default='')   # Nom/objectifs/description mission, phases, conférence préalable, responsable(s) MO
    ref_1_5 = RichTextField(default='')   # Informations fournies par le Maître d'Ouvrage
    ref_1_6 = RichTextField(default='')   # Continuité des activités en aval
    ref_2 = RichTextField(default='')     # Source(s) de financement

    # ===== B. Candidats admis à participer =====
    ref_4_2 = RichTextField(default='')   # AO ouvert ou restreint
    ref_4_3 = RichTextField(default='')   # Liste des candidats admis à participer
    ref_6_4 = RichTextField(default='')   # Renseignements pour la préférence nationale
    ref_7_1 = RichTextField(default='')   # Délai pour demander des éclaircissements
    ref_10 = RichTextField(default='')    # Langue(s) des propositions

    # ===== C. Préparation des offres =====
    ref_11_1 = RichTextField(default='')   # Volumes de l'offre (proposition technique/financière) et contenu
    ref_11_4 = RichTextField(default='')   # Association de consultants figurant sur la liste restreinte
    ref_11_6 = RichTextField(default='')   # Expérience minimale requise du personnel clé
    ref_11_10 = RichTextField(default='')  # La formation comme élément majeur de la mission
    ref_11_12 = RichTextField(default='')  # Monnaie des dépenses locales
    ref_11_14 = RichTextField(default='')  # Durée de validité des propositions

    # ===== D. Dépôt, ouverture, évaluation =====
    ref_18_2 = RichTextField(default='')  # Nombre d'exemplaires à soumettre
    ref_18_3 = RichTextField(default='')  # Montant(s) du (des) cautionnement(s) de soumission par lot
    ref_19_1 = RichTextField(default='')  # Soumission en ligne
    ref_22_1 = RichTextField(default='')  # Lieu, date et heure limite de dépôt des offres
    ref_26_1 = RichTextField(default='')  # Critères d'évaluation retenus par lot
    ref_26_2 = RichTextField(default='')  # Monnaie de conversion et source du taux de change
    ref_26_3 = RichTextField(default='')  # Poids respectifs des propositions technique et financière
    ref_27_1 = RichTextField(default='')  # Lieu des négociations

    # ===== E. Attribution et cautionnement =====
    ref_28 = RichTextField(default='')    # Mode de soumission
    ref_29 = RichTextField(default='')    # Attribution
    ref_30 = RichTextField(default='')    # Taux du cautionnement définitif

    # ===== Champs structurés dérivés (poids des critères) =====
    poids_technique = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    poids_financiere = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.appel_offre}"


class CCAP(models.Model):
    """
    Un champ RichTextField par article du Cahier des Clauses Administratives
    Particulières - Services non quantifiables et prestations intellectuelles
    (DTAO ARMP, articles 1 à 39, pages 89 à 113).
    """
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='ccap_snq')

    objet_marche = RichTextField()                      # Article 1
    procedure_passation = RichTextField()                # Article 2

    # ===== Article 3 : Définitions et attributions =====
    # Réutilisés à l'identique du CCAP conception-réalisation : des champs courts
    # (noms/désignations) plutôt qu'un unique RichTextField, le texte explicatif
    # fixe de chaque rôle étant du texte réglementaire figé dans le template PDF.
    chef_service_marche = models.CharField(max_length=100, default='')
    contractant = models.CharField(max_length=100, blank=True, null=True)
    ing_marche = models.CharField(max_length=100, default='')
    control_externe = models.CharField(max_length=100, default='')
    cocontractant = models.CharField(max_length=100, blank=True, null=True)
    autorite_ordonnancement = models.CharField(max_length=100, default='')
    autorite_liquidation = models.CharField(max_length=100, default='')
    organisme_paiment = models.CharField(max_length=100, default='')
    responsable_renseignement = models.CharField(max_length=100, default='')

    langue_lois_reglements = RichTextField()               # Article 4
    pieces_constitutives_marche = RichTextField()          # Article 5
    textes_generaux_applicables = RichTextField()          # Article 6
    communication = RichTextField()                       # Article 7
    ordres_service = RichTextField()                      # Article 8
    marches_tranches = RichTextField(blank=True, null=True)  # Article 9
    materiel_personnel_cocontractant = RichTextField()     # Article 10
    montant_marche = RichTextField(blank=True, null=True)  # Article 11
    lieu_mode_paiement = RichTextField()                   # Article 12
    garanties_cautions = RichTextField()                   # Article 13
    variation_prix = RichTextField()                       # Article 14
    revision_prix = RichTextField()                        # Article 15
    actualisation_prix = RichTextField()                   # Article 16
    avance_demarrage = RichTextField()                     # Article 17
    reglement_prestations = RichTextField()                # Article 18
    interets_moratoires = RichTextField()                  # Article 19
    penalites = RichTextField()                            # Article 20
    reglement_groupement_soustraitance = RichTextField(blank=True, null=True)  # Article 21
    decompte_general_definitif = RichTextField()           # Article 22
    regime_fiscal_douanier = RichTextField()                # Article 23
    timbres_enregistrement = RichTextField()                # Article 24
    consistance_prestations = RichTextField()               # Article 25
    delais_execution = RichTextField()                      # Article 26
    obligations_maitre_ouvrage = RichTextField()             # Article 27
    obligations_cocontractant = RichTextField()              # Article 28
    assurances = RichTextField()                            # Article 29
    programme_execution = RichTextField()                   # Article 30
    agrement_personnel = RichTextField()                    # Article 31
    sous_traitance = RichTextField(blank=True, null=True)   # Article 32
    commission_suivi_recette = RichTextField()               # Article 33
    recette_prestations = RichTextField()                    # Article 34
    force_majeure = RichTextField()                          # Article 35
    resiliation_marche = RichTextField(blank=True, null=True)  # Article 36
    differends_litiges = RichTextField()                     # Article 37
    edition_diffusion = RichTextField()                      # Article 38
    entree_en_vigueur = RichTextField()                      # Article 39

    def __str__(self):
        return f"{self.appel_offre}"


# Termes de référence (pièce 5) - I à VIII
class TDR(models.Model):
    appel_offre = models.OneToOneField(AppelOffre, on_delete=models.CASCADE, related_name='tdr_snq')
    contexte_justification = RichTextField()      # I. Contexte / justification
    objectif_mission = RichTextField()            # II. Objectif de la mission du prestataire
    consistance_mission = RichTextField()         # III. Consistance de la mission du candidat
    documentation_base = RichTextField()          # IV. Documentation de base
    methodologie = RichTextField()                # V. Méthodologie
    rapports_a_produire = RichTextField()          # VI. Rapports à produire par le prestataire
    calendrier = RichTextField()                  # VII. Calendrier
    profil_consultant = RichTextField()           # VIII. Profil du consultant

    def __str__(self):
        return f"{self.appel_offre}"
