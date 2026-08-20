from rest_framework import serializers
from .models import *


class AAOSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = AvisAppelOffre
        fields = [
            'id', 'appel_offre',

            # ===== Version française =====
            'objet_appel', 'consistence_travaux', 'tranches', 'cout_previsionnel',
            'delai_previsionnel', 'participation', 'financement', 'mode_soumission',
            'caution_soumission', 'consultation_dossier', 'acquisition_dao',
            'remise_offre', 'recevabilite_plis', 'ouverture_plis',
            'critere_eliminatoire', 'critere_essentielles', 'attribution',
            'renseignement_complementaires',

            # ===== Champs communs =====
            'nombre_max_lots', 'duree_validite', 'numero_moa',
            'note_artistique_minimale',

            # ===== Version anglaise =====
            'objet_appel_en', 'consistence_travaux_en', 'tranches_en', 'cout_previsionnel_en',
            'delai_previsionnel_en', 'participation_en', 'financement_en', 'mode_soumission_en',
            'caution_soumission_en', 'consultation_dossier_en', 'acquisition_dao_en',
            'remise_offre_en', 'recevabilite_plis_en', 'ouverture_plis_en',
            'critere_eliminatoire_en', 'critere_essentielles_en', 'attribution_en',
            'renseignement_complementaires_en',

            # ===== Traçabilité traduction =====
            'translated_at', 'valide_en',
        ]
        read_only_fields = ['translated_at']


class RPAOSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = RPAO
        fields = '__all__'


class GrilleNotationSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = GrilleNotation
        fields = '__all__'


class CCAPSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = CCAP
        fields = '__all__'


class TDRSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = TDR
        fields = '__all__'


class CCTPSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = CCTP
        fields = '__all__'


class BPU_DQESerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset=AppelOffre.objects.all()
    )

    class Meta:
        model = BPU_DQE
        fields = '__all__'


class ModelMarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMarche
        fields = '__all__'


