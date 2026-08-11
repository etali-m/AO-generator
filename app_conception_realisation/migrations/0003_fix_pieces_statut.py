from django.db import migrations


# True = pas de formulaire propre (annexe statique ou restitution en lecture seule)
#        => is_complete=True dès la création du dossier
# False = pièce avec formulaire à remplir par l'utilisateur
STATUT_BY_PIECE = {
    'piece1_cr': False,   # AAO
    'piece2_cr': True,    # RGAO - statique
    'piece3_cr': False,   # RPAO
    'piece4_cr': False,   # CCAP
    'piece5_cr': False,   # TDR
    'piece6_cr': False,   # CCTP
    'piece7_cr': False,   # BPU - saisie
    'piece8_cr': True,    # DQE - restitution en lecture seule des mêmes données que la pièce 7
    'piece9_cr': True,    # Sous-détail des prix - statique
    'piece10_cr': False,  # Modèle de marché
    'piece11_cr': True,   # Modèles documents soumissionnaires - statique
    'piece12_cr': True,   # Modèles proposition technique - statique
    'piece13_cr': True,   # Modèles proposition financière - statique
    'piece14_cr': True,   # Charte d'intégrité - statique
    'piece15_cr': True,   # Engagement social et environnemental - statique
    'piece16_cr': True,   # Grilles d'évaluation - restitution en lecture seule (saisie en pièce 3)
    'piece17_cr': False,  # Justificatifs des études préalables
    'piece18_cr': True,   # Liste des banques - statique
    'piece19_cr': True,   # Procédure de soumission en ligne - statique
}


def fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    for nom_composant, statut in STATUT_BY_PIECE.items():
        Piece.objects.filter(nom_composant=nom_composant).update(statut=statut)


def reverse_fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    Piece.objects.filter(nom_composant__in=STATUT_BY_PIECE.keys()).update(statut=False)


class Migration(migrations.Migration):

    dependencies = [
        ('app_conception_realisation', '0002_seed_pieces'),
    ]

    operations = [
        migrations.RunPython(fix_statut, reverse_fix_statut),
    ]
