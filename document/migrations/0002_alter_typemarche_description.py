# Generated by Django 5.1.7 on 2025-04-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typemarche',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
