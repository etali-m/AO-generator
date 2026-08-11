from django.db import migrations


# Piece10 (Modèle de marché) a été reconstruite comme un aperçu en lecture
# seule (sur le modèle de app_travaux/Piece9.vue, qui n'a lui-même aucun
# champ de saisie) : elle ne présente donc plus de formulaire à remplir.
def fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    Piece.objects.filter(nom_composant='piece10_cr').update(statut=True)


def reverse_fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    Piece.objects.filter(nom_composant='piece10_cr').update(statut=False)


class Migration(migrations.Migration):

    dependencies = [
        ('app_conception_realisation', '0003_fix_pieces_statut'),
    ]

    operations = [
        migrations.RunPython(fix_statut, reverse_fix_statut),
    ]
