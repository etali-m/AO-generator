from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User
from document.models import TypeMarche, AppelOffre
from .models import AvisAppelOffre, RPAO, GrilleNotation, CCAP, TDR, CCTP, BPU_DQE, ModelMarche


class ConceptionRealisationFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='qa-cr@example.com',
            first_name='QA',
            last_name='Test',
            phone_number='+237600000001',
            company='QA Corp',
            password='TestPass123!',
        )
        self.user.is_verified = True
        self.user.save()

        self.type_marche = TypeMarche.objects.create(
            nom='Marche de conception et réalisation (test)',
            image_garde='template_marche/conception-realisation.png',
        )

        self.appel_offre = AppelOffre.objects.create(
            user=self.user,
            type_marche=self.type_marche,
            objet_appel="Construction d'un bâtiment administratif",
            maitre_ouvrage='MINTP',
            denomination='MINTP',
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
            'consistence_travaux': '<p>consistance</p>',
            'tranches': '<p>tranches</p>',
            'cout_previsionnel': '<p>cout</p>',
            'delai_previsionnel': '<p>delai</p>',
            'participation': '<p>participation</p>',
            'financement': '<p>financement</p>',
            'mode_soumission': 'en ligne',
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
            'nombre_max_lots': 1,
            'duree_validite': 90,
            'note_artistique_minimale': '70.00',
        }
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/aao', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(AvisAppelOffre.objects.filter(appel_offre=self.appel_offre).count(), 1)

        response = self.client.put(f'/api/marche-conception-realisation/{self.appel_offre.id}/aao', payload, format='json')
        self.assertEqual(response.status_code, 200, response.content)

    def test_grille_notation_bulk_create_and_update(self):
        payload = [
            {'categorie': 'artistique', 'critere': 'Qualité du projet', 'sous_critere': 'Insertion site', 'points': '20.00'},
            {'categorie': 'technique', 'critere': 'Méthodologie', 'sous_critere': None, 'points': '30.00'},
        ]
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/grille_notation', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(GrilleNotation.objects.filter(appel_offre=self.appel_offre).count(), 2)

        response = self.client.put(f'/api/marche-conception-realisation/{self.appel_offre.id}/grille_notation', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(GrilleNotation.objects.filter(appel_offre=self.appel_offre).count(), 2)

    def test_bpu_dqe_bulk_create(self):
        payload = [
            {'type': 'section', 'title': 'SERIE 000', 'code': None, 'designation': None, 'unit': None, 'quantity': '1.00'},
            {'type': 'item', 'title': None, 'code': 'A1', 'designation': 'Terrassement', 'unit': 'm3', 'quantity': '100.00'},
        ]
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/bpu_dqe', payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(BPU_DQE.objects.filter(appel_offre=self.appel_offre).count(), 2)

    def test_tdr_crud(self):
        tdr_payload = {
            'contexte_justification': '<p>contexte</p>',
            'objectif_conception': '<p>objectif</p>',
            'resultats_attendus': '<p>resultats</p>',
            'qualification_consultants': '<p>qualification</p>',
        }
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/tdr', tdr_payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)
        self.assertEqual(TDR.objects.filter(appel_offre=self.appel_offre).count(), 1)

    def test_pdf_generation_end_to_end(self):
        self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/aao', {
            'objet_appel': '<p>objet</p>', 'consistence_travaux': '<p>c</p>', 'tranches': '<p>t</p>',
            'cout_previsionnel': '<p>c</p>', 'delai_previsionnel': '<p>d</p>', 'participation': '<p>p</p>',
            'financement': '<p>f</p>', 'mode_soumission': 'en ligne', 'caution_soumission': '<p>c</p>',
            'consultation_dossier': '<p>c</p>', 'acquisition_dao': '<p>a</p>', 'remise_offre': '<p>r</p>',
            'recevabilite_plis': '<p>r</p>', 'ouverture_plis': '<p>o</p>', 'critere_eliminatoire': '<p>e</p>',
            'critere_essentielles': '<p>e</p>', 'attribution': '<p>a</p>', 'renseignement_complementaires': '<p>r</p>',
            'nombre_max_lots': 1, 'duree_validite': 90,
        }, format='json')

        rpao_fields = [
            'ref_1_1', 'ref_1_2', 'ref_1_4', 'ref_1_5', 'ref_1_6', 'ref_2',
            'ref_4_2', 'ref_5_1', 'ref_6_2', 'ref_7', 'ref_9', 'ref_11',
            'ref_13_2', 'ref_13_3', 'ref_13_4', 'ref_13_7', 'ref_14',
            'ref_15_1', 'ref_16_1', 'ref_16_4', 'ref_17',
            'ref_18', 'ref_19', 'ref_20_3', 'ref_22_5',
            'ref_24', 'ref_25', 'ref_30', 'ref_35', 'ref_36',
        ]
        rpao_payload = {name: '<p>x</p>' for name in rpao_fields}
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/rpao', rpao_payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)

        ccap_fields = [
            'pieces_constitutive_marche', 'textes_applicables', 'communication', 'delai_execution',
            'personnel_entreprise', 'replacement_personnel', 'programme_travaux', 'projet_execution',
            'labo_chantier', 'reunion_chantier', 'operation_prealable_reception', 'commission_reception',
            'documente_a_fournir', 'delai_garantie', 'reception_definitive', 'cautionnement_definitif',
            'cautionnement_garantie', 'cautionnement_avance_demarrage', 'variation_prix', 'revision_prix',
            'actualisation_prix', 'travaux_regie', 'valorisation_approvisionnement', 'avances',
            'decompte_provisoir', 'decompte_final', 'decompte_defintif', 'regime_fiscal', 'force_majeure',
            'differends_litiges', 'edition_marche', 'entree_en_vigueur', 'maitrise_oeuvre_conception',
            'maitre_oeuvre_realisation', 'consistance_phase_conception', 'consistance_phase_realisation',
            'montant_phase1', 'montant_phase2', 'commission_suivi_recette_conception',
        ]
        ccap_payload = {name: '<p>x</p>' for name in ccap_fields}
        ccap_payload.update({
            'chef_service_marche': 'M. X', 'contractant': 'MINTP', 'ing_marche': 'M. Y',
            'control_externe': 'M. Z', 'autorite_ordonnancement': 'Ministre', 'autorite_liquidation': 'DAG',
            'organisme_paiment': 'Trésor', 'responsable_renseignement': 'M. W',
        })
        response = self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/ccap', ccap_payload, format='json')
        self.assertEqual(response.status_code, 201, response.content)

        self.client.post(f'/api/marche-conception-realisation/{self.appel_offre.id}/bpu_dqe', [
            {'type': 'section', 'title': 'SERIE 000'},
            {'type': 'item', 'code': 'A1', 'designation': 'Terrassement', 'unit': 'm3', 'quantity': '100.00'},
        ], format='json')

        response = self.client.get(f'/api/marche-conception-realisation/{self.appel_offre.id}/apercu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertGreater(len(response.content), 1000)
