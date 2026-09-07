from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User
from document.models import TypeMarche, AppelOffre
from .models import AvisAppelOffre, RPAO, CCAP, TDR


class ServicesNonQuantifiablesFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='qa-snq@example.com',
            first_name='QA',
            last_name='Test',
            phone_number='+237600000002',
            company='QA Corp',
            password='TestPass123!',
        )
        self.user.is_verified = True
        self.user.save()

        self.type_marche = TypeMarche.objects.create(
            nom='Marché de Services Non Quantifiables (test)',
            image_garde='template_marche/services-non-quantifiables.png',
        )

        self.appel_offre = AppelOffre.objects.create(
            user=self.user,
            type_marche=self.type_marche,
            objet_appel="Recrutement d'un bureau d'études",
            maitre_ouvrage='MINEPAT',
            denomination='MINEPAT',
            commission_marche='cipm',
            type_dossier='national',
            mode_passation='ouvert',
            numero_dossier=1,
            exercice_budgetaire=2026,
            financement='Budget national',
            imputation='65 800',
        )

        token = RefreshToken.for_user(self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

    def test_aao_create_and_update(self):
        payload = {
            'objet_appel': '<p>objet</p>',
            'consistence_prestations': '<p>consistance</p>',
            'tranches': '<p>tranches</p>',
            'cout_previsionnel': '<p>cout</p>',
            'delai_previsionnel': '<p>delai</p>',
            'participation': '<p>participation</p>',
            'financement': '<p>financement</p>',
            'mode_soumission': '<p>mode</p>',
            'caution_soumission': '<p>caution</p>',
            'consultation_dossier': '<p>consultation</p>',
            'acquisition_dao': '<p>acquisition</p>',
            'remise_offre': '<p>remise</p>',
            'recevabilite_plis': '<p>recevabilite</p>',
            'ouverture_plis': '<p>ouverture</p>',
            'critere_eliminatoire': '<p>eliminatoire</p>',
            'critere_essentielles': '<p>essentielles</p>',
            'attribution': '<p>attribution</p>',
            'renseignement_complementaires': '<p>renseignements</p>',
            'duree_validite': 90,
            'nombre_max_lots': 1,
        }
        response = self.client.post(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/aao', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(AvisAppelOffre.objects.filter(appel_offre=self.appel_offre).count(), 1)

        response = self.client.put(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/aao', payload, format='json')
        self.assertEqual(response.status_code, 200, response.content)

    def test_rpao_crud(self):
        payload = {'ref_1_1': '<p>ref 1.1</p>', 'ref_2': '<p>financement</p>'}
        response = self.client.post(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/rpao', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(RPAO.objects.filter(appel_offre=self.appel_offre).count(), 1)

    def test_ccap_crud(self):
        payload = {
            'objet_marche': '<p>objet</p>',
            'procedure_passation': '<p>procedure</p>',
            'chef_service_marche': 'Le Chef de Service X',
            'ing_marche': "L'Ingénieur Y",
            'control_externe': 'Ministère des Marchés Publics',
            'cocontractant': 'Bureau Z',
            'autorite_ordonnancement': 'Le Ministre A',
            'autorite_liquidation': 'Le Ministre A',
            'organisme_paiment': 'Trésor Public',
            'responsable_renseignement': 'Le Chef de Service X',
            'langue_lois_reglements': '<p>langue</p>',
            'pieces_constitutives_marche': '<p>pieces</p>',
            'textes_generaux_applicables': '<p>textes</p>',
            'communication': '<p>communication</p>',
            'ordres_service': '<p>ordres</p>',
            'materiel_personnel_cocontractant': '<p>materiel</p>',
            'lieu_mode_paiement': '<p>paiement</p>',
            'garanties_cautions': '<p>garanties</p>',
            'variation_prix': '<p>variation</p>',
            'revision_prix': '<p>revision</p>',
            'actualisation_prix': '<p>actualisation</p>',
            'avance_demarrage': '<p>avance</p>',
            'reglement_prestations': '<p>reglement</p>',
            'interets_moratoires': '<p>interets</p>',
            'penalites': '<p>penalites</p>',
            'decompte_general_definitif': '<p>decompte</p>',
            'regime_fiscal_douanier': '<p>fiscal</p>',
            'timbres_enregistrement': '<p>timbres</p>',
            'consistance_prestations': '<p>consistance</p>',
            'delais_execution': '<p>delais</p>',
            'obligations_maitre_ouvrage': '<p>obligations mo</p>',
            'obligations_cocontractant': '<p>obligations co</p>',
            'assurances': '<p>assurances</p>',
            'programme_execution': '<p>programme</p>',
            'agrement_personnel': '<p>agrement</p>',
            'commission_suivi_recette': '<p>commission</p>',
            'recette_prestations': '<p>recette</p>',
            'force_majeure': '<p>force majeure</p>',
            'differends_litiges': '<p>differends</p>',
            'edition_diffusion': '<p>edition</p>',
            'entree_en_vigueur': '<p>entree vigueur</p>',
        }
        response = self.client.post(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/ccap', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(CCAP.objects.filter(appel_offre=self.appel_offre).count(), 1)

    def test_tdr_crud(self):
        payload = {
            'contexte_justification': '<p>contexte</p>',
            'objectif_mission': '<p>objectif</p>',
            'consistance_mission': '<p>consistance</p>',
            'documentation_base': '<p>documentation</p>',
            'methodologie': '<p>methodologie</p>',
            'rapports_a_produire': '<p>rapports</p>',
            'calendrier': '<p>calendrier</p>',
            'profil_consultant': '<p>profil</p>',
        }
        response = self.client.post(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/tdr', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(TDR.objects.filter(appel_offre=self.appel_offre).count(), 1)

    def test_pdf_generation_end_to_end(self):
        response = self.client.get(f'/api/marche-services-non-quantifiables/{self.appel_offre.id}/apercu/')
        self.assertEqual(response.status_code, 200, response.content[:500])
        self.assertEqual(response['Content-Type'], 'application/pdf')
