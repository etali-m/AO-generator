from django.db import migrations


PIECES = [
    ("piece1_cr", "Avis d'Appel d'Offres (AAO)"),
    ("piece2_cr", "Règlement Général de l'Appel d'Offres (RGAO)"),
    ("piece3_cr", "Règlement Particulier de l'Appel d'Offres (RPAO)"),
    ("piece4_cr", "Cahier des Clauses Administratives Particulières (CCAP)"),
    ("piece5_cr", "Termes de Référence (TDR)"),
    ("piece6_cr", "Cahier des Clauses Techniques Particulières (CCTP)"),
    ("piece7_cr", "Cadre du Bordereau des Prix Unitaires"),
    ("piece8_cr", "Cadre du Détail Quantitatif et Estimatif"),
    ("piece9_cr", "Cadre du Sous-Détail des Prix ou Décomposition des Prix Forfaitaires"),
    ("piece10_cr", "Modèle de Marché"),
    ("piece11_cr", "Modèles de Documents à Utiliser par les Soumissionnaires"),
    ("piece12_cr", "Modèles des Pièces et Tableaux Types pour la Proposition Technique"),
    ("piece13_cr", "Modèles des Pièces et Tableaux Types pour la Proposition Financière"),
    ("piece14_cr", "Charte d'Intégrité"),
    ("piece15_cr", "Engagement Social et Environnemental"),
    ("piece16_cr", "Grilles d'Évaluation"),
    ("piece17_cr", "Justificatifs des Études Préalables"),
    ("piece18_cr", "Liste des Établissements Bancaires et Organismes Financiers Autorisés"),
    ("piece19_cr", "Procédure de Soumission en Ligne"),
]


def seed_pieces(apps, schema_editor):
    TypeMarche = apps.get_model('document', 'TypeMarche')
    Piece = apps.get_model('document', 'Piece')

    type_marche, _ = TypeMarche.objects.get_or_create(
        slug='marche-de-conception-et-realisation',
        defaults={
            'nom': 'Marche de conception et réalisation',
            'image_garde': 'template_marche/conception-realisation.png',
        },
    )

    for index, (nom_composant, titre) in enumerate(PIECES, start=1):
        piece, created = Piece.objects.get_or_create(
            type_marche=type_marche,
            nom_composant=nom_composant,
            defaults={'titre': titre, 'statut': False},
        )
        if not created and piece.titre != titre:
            piece.titre = titre
            piece.save(update_fields=['titre'])

    # La pièce 1 (AAO) avait été créée manuellement avant cette migration
    # sous un autre nom de composant ("AAO_conception") : on la normalise
    # pour qu'elle corresponde à la convention piece1_cr utilisée partout ailleurs.
    Piece.objects.filter(
        type_marche=type_marche,
        nom_composant='AAO_conception',
    ).exclude(nom_composant='piece1_cr').update(nom_composant='__AAO_conception_legacy__')

    legacy = Piece.objects.filter(
        type_marche=type_marche,
        nom_composant='__AAO_conception_legacy__',
    ).first()
    if legacy is not None:
        # S'il existe déjà une piece1_cr distincte (créée par la boucle ci-dessus),
        # on supprime le doublon hérité plutôt que de violer l'unicité du nom_composant.
        if Piece.objects.filter(type_marche=type_marche, nom_composant='piece1_cr').exclude(pk=legacy.pk).exists():
            legacy.delete()
        else:
            legacy.nom_composant = 'piece1_cr'
            legacy.titre = PIECES[0][1]
            legacy.save(update_fields=['nom_composant', 'titre'])


def unseed_pieces(apps, schema_editor):
    TypeMarche = apps.get_model('document', 'TypeMarche')
    Piece = apps.get_model('document', 'Piece')
    try:
        type_marche = TypeMarche.objects.get(slug='marche-de-conception-et-realisation')
    except TypeMarche.DoesNotExist:
        return
    Piece.objects.filter(
        type_marche=type_marche,
        nom_composant__in=[nom for nom, _ in PIECES],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('app_conception_realisation', '0001_initial'),
        ('document', '0013_appeloffre_departement_appeloffre_logo_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_pieces, unseed_pieces),
    ]
