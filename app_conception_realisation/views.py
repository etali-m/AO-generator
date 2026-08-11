from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import pdfkit
import base64
import os
import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from .models import *
from .serializers import *
import logging
from services.translation import build_translated_fields
from django.utils import timezone
logger = logging.getLogger(__name__)


class AAOView(GenericAPIView):
    serializer_class = AAOSerializer
    queryset = AvisAppelOffre.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        extra_fields = self._get_translation_kwargs(serializer.validated_data)
        serializer.save(**extra_fields)

        return Response({
            'data': serializer.data,
            'message': "Avis d'Appel d'Offre enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = AvisAppelOffre.objects.get(appel_offre=project_id)
        except AvisAppelOffre.DoesNotExist:
            return Response(
                {'detail': "L'avis d'appel d'offre n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)

        extra_fields = self._get_translation_kwargs(serializer.validated_data)
        serializer.save(**extra_fields)

        return Response({
            'data': serializer.data,
            'message': "Avis d'Appel d'Offre a été mis à jour correctement"
        }, status=status.HTTP_200_OK)

    def _get_translation_kwargs(self, validated_data):
        try:
            translated = build_translated_fields(validated_data)
            if not translated:
                return {}
            translated['translated_at'] = timezone.now()
            translated['valide_en'] = False
            return translated
        except Exception as e:
            logger.error(f"Échec de la traduction automatique pour project_id={self.kwargs.get('project_id')}: {e}")
            return {}


class RPAOView(GenericAPIView):
    serializer_class = RPAOSerializer
    queryset = RPAO.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Règlement particulier enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = RPAO.objects.get(appel_offre=project_id)
        except RPAO.DoesNotExist:
            return Response(
                {'detail': "Le RPAO n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Le RPAO a été mis à jour correctement"
        }, status=status.HTTP_200_OK)


class GrilleNotationView(GenericAPIView):
    serializer_class = GrilleNotationSerializer
    queryset = GrilleNotation.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Grille de notation enregistrée avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()

        GrilleNotation.objects.filter(appel_offre=project_id).delete()

        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "La grille de notation a été mise à jour correctement"
        }, status=status.HTTP_201_CREATED)


class CCAPView(GenericAPIView):
    serializer_class = CCAPSerializer
    queryset = CCAP.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "CCAP enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = CCAP.objects.get(appel_offre=project_id)
        except CCAP.DoesNotExist:
            return Response(
                {'detail': "Le CCAP n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Le CCAP a été mis à jour correctement"
        }, status=status.HTTP_200_OK)


class TDRView(GenericAPIView):
    serializer_class = TDRSerializer
    queryset = TDR.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Termes de référence enregistrés avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = TDR.objects.get(appel_offre=project_id)
        except TDR.DoesNotExist:
            return Response(
                {'detail': "Les termes de référence n'existent pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Les termes de référence ont été mis à jour correctement"
        }, status=status.HTTP_200_OK)


class CCTPView(GenericAPIView):
    serializer_class = CCTPSerializer
    queryset = CCTP.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "CCTP enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = CCTP.objects.get(appel_offre=project_id)
        except CCTP.DoesNotExist:
            return Response(
                {'detail': "Le CCTP n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Le CCTP a été mis à jour correctement"
        }, status=status.HTTP_200_OK)


class BPU_DQEView(GenericAPIView):
    serializer_class = BPU_DQESerializer
    queryset = BPU_DQE.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Bordereau de prix enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()

        BPU_DQE.objects.filter(appel_offre=project_id).delete()

        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Le BPU et le DQE ont été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)


class ModelMarcheView(GenericAPIView):
    serializer_class = ModelMarcheSerializer
    queryset = ModelMarche.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Modèle de marché enregistré avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = ModelMarche.objects.get(appel_offre=project_id)
        except ModelMarche.DoesNotExist:
            return Response(
                {'detail': "Le Modèle de marché n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Le Modèle a été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)


class EtudePrealableView(GenericAPIView):
    serializer_class = EtudePrealableSerializer
    queryset = EtudePrealable.objects.all()

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        queryset = self.get_queryset().filter(appel_offre=project_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Justificatifs des études préalables enregistrés avec succès"
        }, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = EtudePrealable.objects.get(appel_offre=project_id)
        except EtudePrealable.DoesNotExist:
            return Response(
                {'detail': "Les justificatifs des études préalables n'existent pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Les justificatifs des études préalables ont été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)


def get_image_base64(image_field):
    """Convertit un ImageField Django en base64 pour l'intégrer dans le HTML"""
    if not image_field:
        return None

    try:
        image_path = os.path.join(settings.MEDIA_ROOT, str(image_field))

        if not os.path.exists(image_path):
            return None

        extension = os.path.splitext(image_path)[1].lower()
        mime_types = {
            '.jpg':  'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png':  'image/png',
            '.gif':  'image/gif',
            '.webp': 'image/webp',
            '.svg':  'image/svg+xml',
        }
        mime_type = mime_types.get(extension, 'image/png')

        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        return f"data:{mime_type};base64,{image_data}"

    except Exception as e:
        print(f"Erreur encodage image : {e}")
        return None


def generer_pdf(request, project_id, mode='inline'):
    appel_offre = get_object_or_404(AppelOffre, id=project_id)

    aao = AvisAppelOffre.objects.filter(appel_offre=appel_offre).first()
    rpao = RPAO.objects.filter(appel_offre=appel_offre).first()
    ccap = CCAP.objects.filter(appel_offre=appel_offre).first()
    tdr = TDR.objects.filter(appel_offre=appel_offre).first()
    cctp = CCTP.objects.filter(appel_offre=appel_offre).first()
    etude_prealable = EtudePrealable.objects.filter(appel_offre=appel_offre).first()
    bpu_dqe = BPU_DQE.objects.filter(appel_offre=appel_offre)
    grille_notation = GrilleNotation.objects.filter(appel_offre=appel_offre)

    logo_base64 = get_image_base64(appel_offre.logo)

    context = {
        'appel_offre': appel_offre,
        'aao': aao,
        'rpao': rpao,
        'ccap': ccap,
        'tdr': tdr,
        'cctp': cctp,
        'etude_prealable': etude_prealable,
        'bpu_dqe': bpu_dqe,
        'grille_notation': grille_notation,
        'logo_base64': logo_base64,
    }

    template = loader.get_template('app_conception_realisation/dao_conception_realisation.html')
    html = template.render(context)

    config = pdfkit.configuration(
        wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    )
    options = {
        'encoding': 'UTF-8',
        'enable-local-file-access': '',
        'quiet': '',
    }

    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        pdfkit.from_string(html, tmp_path, configuration=config, options=options)

        with open(tmp_path, 'rb') as f:
            pdf = f.read()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    nom_fichier = f"appel_offre_{appel_offre.numero_dossier or project_id}.pdf"
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'{mode}; filename="{nom_fichier}"'

    return response


def apercu_marche_conception_realisation(request, project_id):
    return generer_pdf(request, project_id, mode='inline')


def telecharger_marche_conception_realisation(request, project_id):
    return generer_pdf(request, project_id, mode='attachment')
