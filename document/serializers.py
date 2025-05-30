from rest_framework import serializers
from .models import TypeMarche, AppelOffre, Piece
from account.models import User

class TypeMarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMarche
        fields = ['id', 'nom', 'description', 'slug', 'image_garde']


class PieceSerializer(serializers.ModelSerializer):
    type_marche = serializers.PrimaryKeyRelatedField(
        queryset=TypeMarche.objects.all()
    )
    class Meta:
        model = Piece
        fields = ['id', 'type_marche', 'titre', 'description', 'nom_composant']


class AppelOffreSerializer(serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    type_marche = serializers.PrimaryKeyRelatedField(
        queryset=TypeMarche.objects.all()
    )

    class Meta:
        model = AppelOffre
        fields = [ 'id', 'type_marche', 'user', 'objet_appel', 'maitre_ouvrage', 'denomination', 'commission_marche', 'type_dossier', 'numero_dossier', 'exercice_budgetaire', 'financement', 'imputation']

