from rest_framework import serializers
from .models import *

class AAOSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = AvisAppelOffre
        fields = ['id', 'appel_offre', 'objet_appel', 'consistence_travaux', 'tranches', 'cout_previsionnel', 'delai_previsionnel', 'participation', 'financement', 'mode_soumission', 'caution_soumission', 'consultation_dossier', 'acquisition_dao', 'remise_offre', 'recevabilite_plis', 'ouverture_plis', 'critere_eliminatoire', 'critere_essentielles', 'attribution', 'nombre_max_lots', 'duree_validite', 'renseignement_complementaires', 'numero_moa']                                                                                                   
#reglèment général de l'appel d'offre.
class RPAOSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = RPAO
        fields = '__all__'


#reglèment particulier de l'appel d'offre.
class CCAPSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = CCAP
        fields = '__all__'

#Cahier des Clause Techniques Particulières
class CCTPSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = CCTP
        fields = '__all__'


#Bordereau des prix unitaires
class BPUSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = BPU
        fields = '__all__'

#BDevis Quantitatif et Estimatif
class DQESerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AppelOffre.objects.all()
    )

    class Meta:
        model = DQE
        fields = '__all__'


class ModelMarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMarche
        fields = '__all__'