# Generated by Django 5.2 on 2025-07-08 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_travaux', '0010_bpu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bpu',
            old_name='borderau',
            new_name='prix_unitaires',
        ),
    ]
