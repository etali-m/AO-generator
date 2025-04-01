from django.db import models

# Create your models here.
class TypeMarche(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_garde = models.ImageField(upload_to='template_marche/')

    def __str__(self):
        return f'{self.nom}'