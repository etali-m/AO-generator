# services/translation.py
import os
import logging
from django.utils import timezone
import deepl

logger = logging.getLogger(__name__)
translator = deepl.Translator(os.environ["DEEPL_API_KEY"])

TRANSLATABLE_FIELDS = [
    'objet_appel', 'consistence_travaux', 'tranches', 'cout_previsionnel',
    'delai_previsionnel', 'participation', 'financement', 'mode_soumission',
    'caution_soumission', 'consultation_dossier', 'acquisition_dao',
    'remise_offre', 'recevabilite_plis', 'ouverture_plis',
    'critere_eliminatoire', 'critere_essentielles', 'attribution',
    'renseignement_complementaires',
]


def build_translated_fields(validated_data):
    """
    Prend le validated_data d'un AAOSerializer (avant save), traduit les champs
    français présents via DeepL, et retourne un dict {champ_en: valeur} prêt
    à être passé en kwargs à serializer.save(). Ne fait AUCUNE requête SQL.
    """
    # On ne garde que les champs non vides, dans un ordre stable
    fields_present = [
        field for field in TRANSLATABLE_FIELDS
        if validated_data.get(field)
    ]
    if not fields_present:
        return {}

    texts = [validated_data[field] for field in fields_present]

    # Un seul appel API pour tous les champs à la fois (liste de textes)
    results = translator.translate_text(
        texts,
        source_lang="FR",
        target_lang="EN-US",   # ou "EN-GB" selon la convention souhaitée
        tag_handling="html",   # préserve automatiquement les balises HTML
        preserve_formatting=True,
    )

    translated = {
        f"{field}_en": result.text
        for field, result in zip(fields_present, results)
    }
    return translated