# Generated by Django 5.2 on 2025-07-07 13:28

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_travaux', '0008_alter_rpao_liste_prequalifie_and_more'),
        ('document', '0012_remove_appeloffre_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_service_marche', models.CharField(max_length=100)),
                ('ing_marche', models.CharField(max_length=100)),
                ('control_externe', models.CharField(max_length=100)),
                ('cocontractant', models.CharField(blank=True, max_length=100, null=True)),
                ('autorite_ordonnancement', models.CharField(max_length=100)),
                ('autorite_liquidation', models.CharField(max_length=100)),
                ('organisme_paiment', models.CharField(max_length=100)),
                ('responsable_renseignement', models.CharField(max_length=100)),
                ('pieces_constitutive_marche', ckeditor.fields.RichTextField()),
                ('textes_applicables', ckeditor.fields.RichTextField()),
                ('communication', ckeditor.fields.RichTextField()),
                ('delai_execution', ckeditor.fields.RichTextField()),
                ('marche_a_tranche', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('personnel_entreprise', ckeditor.fields.RichTextField()),
                ('replacement_personnel', ckeditor.fields.RichTextField()),
                ('programme_travaux', ckeditor.fields.RichTextField()),
                ('projet_execution', ckeditor.fields.RichTextField()),
                ('labo_chantier', ckeditor.fields.RichTextField()),
                ('reunion_chantier', ckeditor.fields.RichTextField()),
                ('utilisation_explosifs', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('operation_prealable_reception', ckeditor.fields.RichTextField()),
                ('commission_reception', ckeditor.fields.RichTextField()),
                ('reception_partielle', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('periode_garantie', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('documente_a_fournir', ckeditor.fields.RichTextField()),
                ('delai_garantie', ckeditor.fields.RichTextField()),
                ('reception_definitive', ckeditor.fields.RichTextField()),
                ('cautionnement_definitif', ckeditor.fields.RichTextField()),
                ('cautionnement_garantie', ckeditor.fields.RichTextField()),
                ('cautionnement_avance_demarrage', ckeditor.fields.RichTextField()),
                ('variation_prix', ckeditor.fields.RichTextField()),
                ('revision_prix', ckeditor.fields.RichTextField()),
                ('actualisation_prix', ckeditor.fields.RichTextField()),
                ('travaux_regie', ckeditor.fields.RichTextField()),
                ('valorisation_approvisionnement', ckeditor.fields.RichTextField()),
                ('avances', ckeditor.fields.RichTextField()),
                ('decompte_provisoir', ckeditor.fields.RichTextField()),
                ('decompte_final', ckeditor.fields.RichTextField()),
                ('decompte_defintif', ckeditor.fields.RichTextField()),
                ('reglement_groupement', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('regime_fiscal', ckeditor.fields.RichTextField()),
                ('resiliation_marche', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('force_majeure', ckeditor.fields.RichTextField()),
                ('differends_litiges', ckeditor.fields.RichTextField()),
                ('edition_marche', ckeditor.fields.RichTextField()),
                ('entree_en_vigueur', ckeditor.fields.RichTextField()),
                ('appel_offre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.appeloffre')),
            ],
        ),
    ]
