from django.db import migrations


# Piece0 (Lettre d'invitation à soumissionner) est préparée séparément par le
# Maître d'Ouvrage et simplement insérée lors de l'impression du dossier : ce
# n'est plus une pièce-formulaire à remplir dans l'application.
def fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    Piece.objects.filter(nom_composant='piece0_snq').update(statut=True)


def reverse_fix_statut(apps, schema_editor):
    Piece = apps.get_model('document', 'Piece')
    Piece.objects.filter(nom_composant='piece0_snq').update(statut=False)


class Migration(migrations.Migration):

    dependencies = [
        ('app_services_non_quantifiables', '0003_delete_lettreinvitation'),
    ]

    operations = [
        migrations.RunPython(fix_statut, reverse_fix_statut),
    ]
