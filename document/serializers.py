from rest_framework import serializers
from .models import TypeMarche, AppelOffre

class TypeMarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMarche
        fields = ['id', 'nom', 'description', 'slug', 'image_garde']


class AppelOffreSerializer(serializers.ModelSerializer): 
    type_marche = serializers.PrimaryKeyRelatedField(
        queryset=TypeMarche.objects.all(), write_only=True
    )

    class Meta:
        model = AppelOffre
        fields = ['type_marche', 'objet_appel', 'maitre_ouvrage', 'denomination', 'commission_marche', 'type_dossier', 'numero_dossier', 'exercice_budgetaire', 'financement', 'imputation']