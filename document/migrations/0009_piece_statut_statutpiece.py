# Generated by Django 5.2 on 2025-06-03 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0008_appeloffre_mode_passation'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='statut',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='StatutPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False)),
                ('appel_offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pieces', to='document.appeloffre')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.piece')),
            ],
            options={
                'unique_together': {('appel_offre', 'piece')},
            },
        ),
    ]
