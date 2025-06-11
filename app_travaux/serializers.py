from rest_framework import serializers
from .models import *

class AAOSerializer(serializers.ModelSerializer):
    appel_offre = serializers.PrimaryKeyRelatedField(
        queryset = AvisAppelOffre.objects.all()
    )

    class Meta:
        model = AvisAppelOffre
        fields = ['appel_offre', 'objet_appel', 'consistence_travaux', 'tranches', 'cout_previsionnel', 'delai_previsionnel', 'participation', 'financement', 'mode_soumission', 'caution_soumission', 'consultation_dossier', 'acquisition_dao', 'remise_offre', 'recevabilite_plis', 'ouverture_plis', 'critere_eliminatoire', 'critere_essentielles', 'attribution', 'nombre_max_lots', 'duree_validite', 'renseignement_complementaires', 'numero_moa']