from modeltranslation.translator import translator, TranslationOptions
from .models import AvisAppelOffre

class AvisAppelOffreTranslationOptions(TranslationOptions):
    fields = (
        'objet_appel',
        'consistence_travaux',
        'tranches',
        'cout_previsionnel',
        'delai_previsionnel',
        'participation',
        'financement',
        'mode_soumission',
        'caution_soumission',
        'consultation_dossier',
        'acquisition_dao',
        'remise_offre',
        'recevabilite_plis',
        'ouverture_plis',
        'critere_eliminatoire',
        'critere_essentielles',
        'attribution',
        'renseignement_complementaires',
    )

translator.register(AvisAppelOffre, AvisAppelOffreTranslationOptions)
