from django.db import migrations


# Les migrations 0003/0004 ont corrigé le statut PAR DEFAUT des pièces (utilisé
# uniquement à la création d'un nouveau dossier). Cette migration synchronise
# rétroactivement les dossiers déjà existants (créés avant ces correctifs) afin
# que les pièces sans formulaire (statut=True) apparaissent bien "complètes"
# dans la liste, y compris pour des dossiers créés avant le correctif.
def sync_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    StatutPiece = apps.get_model('document', 'StatutPiece')

    pieces_toujours_completes = Piece.objects.filter(
        type_marche__slug='marche-de-conception-et-realisation',
        statut=True,
    )
    updated = StatutPiece.objects.filter(
        piece__in=pieces_toujours_completes,
        is_complete=False,
    ).update(is_complete=True)
    print(f"{updated} StatutPiece existants synchronisés")


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('app_conception_realisation', '0004_fix_piece10_statut'),
    ]

    operations = [
        migrations.RunPython(sync_statut, noop),
    ]
