from rest_framework import serializers
from .models import TypeMarche, AppelOffre, Piece, StatutPiece
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
    numero_appel_offre = serializers.SerializerMethodField() #numero d'appel d'offre généré par la fonction 
    titre_complet = serializers.SerializerMethodField()

    #pour avoir tous les elements du type de marche dans le serializer
    #type_marche = TypeMarcheSerializer(read_only=True)

    # Récupérer juste le nom du type de marché (lecture seule)
    type_marche_nom = serializers.CharField(source='type_marche.nom', read_only=True)
    type_marche_slug = serializers.CharField(source='type_marche.slug', read_only=True)
    class Meta:
        model = AppelOffre
        fields = [ 'id', 'type_marche', 'type_marche_nom', 'type_marche_slug', 'user', 'objet_appel', 'maitre_ouvrage', 'denomination', 'commission_marche', 'type_dossier', 'mode_passation', 'numero_dossier', 'exercice_budgetaire', 'financement', 'imputation', 'numero_appel_offre', 'date_creation', 'titre_complet']
    
    def get_numero_appel_offre(self, obj):
        return obj.numero_appel_offre
    
    def get_titre_complet(self, obj):
        return obj.titre_complet


#serializer en lecture seul pour uniquement lire statutPiece
class StatutPieceSerializer(serializers.ModelSerializer):
    piece = PieceSerializer(read_only=True)
    appel_offre = AppelOffreSerializer(read_only=True)

    class Meta:
        model = StatutPiece
        fields = ['id', 'appel_offre', 'piece', 'is_complete']

#Mettre à jour statutPiece
class UpdateStatutPieceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = StatutPiece
        fields = ['is_complete']