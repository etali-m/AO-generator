from django.db import migrations


# (nom_composant, titre, statut)
# statut=True  -> pièce statique, marquée complète dès la création du dossier
# statut=False -> pièce-formulaire, à compléter par le Maître d'Ouvrage
PIECES = [
    ("piece0_snq", "Lettre d'Invitation à Soumissionner (le cas échéant)", False),
    ("piece1_snq", "Avis d'Appel d'Offres (AAO)", False),
    ("piece2_snq", "Règlement Général de l'Appel d'Offres (RGAO)", True),
    ("piece3_snq", "Règlement Particulier de l'Appel d'Offres (RPAO)", False),
    ("piece4_snq", "Cahier des Clauses Administratives Particulières (CCAP)", False),
    ("piece5_snq", "Termes de Référence (TDR)", False),
    ("piece6_snq", "Proposition Technique - Tableaux Types", True),
    ("piece7_snq", "Proposition Financière - Tableaux Types", True),
    ("piece8_snq", "Modèle de Marché", True),
    ("piece9_snq", "Modèles ou Formulaires Types à Utiliser par les Soumissionnaires", True),
    ("piece10_snq", "Charte d'Intégrité", True),
    ("piece11_snq", "Déclaration d'Engagement au Respect des Clauses Sociales et Environnementales", True),
    ("piece12_snq", "Visa de Maturité ou Justificatifs des Études Préalables", True),
    ("piece13_snq", "Liste des Établissements Bancaires et Organismes Financiers Habilités", True),
    ("piece14_snq", "Procédure de Soumission en Ligne", True),
]


def seed_pieces(apps, schema_editor):
    TypeMarche = apps.get_model('document', 'TypeMarche')
    Piece = apps.get_model('document', 'Piece')

    type_marche, _ = TypeMarche.objects.get_or_create(
        slug='marche-de-services-non-quantifiables',
        defaults={
            'nom': 'Marché de Services Non Quantifiables et Prestations Intellectuelles',
            'image_garde': 'template_marche/services-non-quantifiables.png',
        },
    )

    for nom_composant, titre, statut in PIECES:
        piece, created = Piece.objects.get_or_create(
            type_marche=type_marche,
            nom_composant=nom_composant,
            defaults={'titre': titre, 'statut': statut},
        )
        if not created and (piece.titre != titre or piece.statut != statut):
            piece.titre = titre
            piece.statut = statut
            piece.save(update_fields=['titre', 'statut'])


def unseed_pieces(apps, schema_editor):
    TypeMarche = apps.get_model('document', 'TypeMarche')
    Piece = apps.get_model('document', 'Piece')
    try:
        type_marche = TypeMarche.objects.get(slug='marche-de-services-non-quantifiables')
    except TypeMarche.DoesNotExist:
        return
    Piece.objects.filter(
        type_marche=type_marche,
        nom_composant__in=[nom for nom, _, _ in PIECES],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('app_services_non_quantifiables', '0001_initial'),
        ('document', '0013_appeloffre_departement_appeloffre_logo_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_pieces, unseed_pieces),
    ]
