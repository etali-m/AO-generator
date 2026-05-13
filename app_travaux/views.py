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

# Create your views here.
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
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Avis d'Appel d'Offre enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un AAO
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
        serializer.save()

        return Response({ 
            'data': serializer.data,
            'message': "Avis d'Appel d'Offre a été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)
    

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
            'message': "Règlement particulier enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un RPAO
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
            'message': "Avis d'Appel d'Offre a été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)
    

#ccap travaux view
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
            'message': "CCAP enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un CCAP
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
        }, status=status.HTTP_201_CREATED)
   

#cctp travaux view
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
            'message': "CCTP enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un CCTP
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
        }, status=status.HTTP_201_CREATED)


#BPU travaux view
class BPUView(GenericAPIView):
    serializer_class = BPUSerializer
    queryset = BPU.objects.all()

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
            'message': "BPY enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un CCAP
    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = BPU.objects.get(appel_offre=project_id)
        except BPU.DoesNotExist:
            return Response(
                {'detail': "Le BPU n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({ 
            'data': serializer.data,
            'message': "Le BPU a été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)


#DQE travaux view
class DQEView(GenericAPIView):
    serializer_class = DQESerializer
    queryset = DQE.objects.all()

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
            'message': "DQE enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un DQE
    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy()
        data['appel_offre'] = project_id

        try:
            instance = DQE.objects.get(appel_offre=project_id)
        except DQE.DoesNotExist:
            return Response(
                {'detail': "Le BPU n'existe pas"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({ 
            'data': serializer.data,
            'message': "Le BPU a été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)
    

#DQE travaux view
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
        # AJOUTER appel_offre SUR CHAQUE LIGNE
        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data,
            'message': "Borderau de prix enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un DQE
    def put(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        data = request.data.copy() 

         # supprimer anciennes lignes
        BPU_DQE.objects.filter(
            appel_offre=project_id
        ).delete()

         # ajouter FK
        for item in data:
            item['appel_offre'] = int(project_id)

        serializer = self.get_serializer(
            data=data,
            many=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({ 
            'data': serializer.data,
            'message': "Le BPU et le DQE ont été mis à jour correctement"
        }, status=status.HTTP_201_CREATED)


#Modèle de marché travaux view
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
            'message': "Modèle de marché enregsitré avec succès"
        }, status=status.HTTP_201_CREATED)
    
    #Mise à jour d'un DQE
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
    

def get_image_base64(image_field):
    """Convertit un ImageField Django en base64 pour l'intégrer dans le HTML"""
    if not image_field:
        return None
    
    try:
        # Construire le chemin absolu vers le fichier
        image_path = os.path.join(settings.MEDIA_ROOT, str(image_field))
        
        if not os.path.exists(image_path):
            return None
        
        # Détecter le type MIME selon l'extension
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
        
        # Lire et encoder en base64
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        return f"data:{mime_type};base64,{image_data}"
    
    except Exception as e:
        print(f"Erreur encodage image : {e}")
        return None

  
def get_image_base64(image_field):
    """Convertit un ImageField Django en base64 pour l'intégrer dans le HTML"""
    if not image_field:
        return None
    
    try:
        # Construire le chemin absolu vers le fichier
        image_path = os.path.join(settings.MEDIA_ROOT, str(image_field))
        
        if not os.path.exists(image_path):
            return None
        
        # Détecter le type MIME selon l'extension
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
        
        # Lire et encoder en base64
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        return f"data:{mime_type};base64,{image_data}"
    
    except Exception as e:
        print(f"Erreur encodage image : {e}")
        return None
 

def generer_pdf(request, project_id, mode='inline'):
    appel_offre = get_object_or_404(AppelOffre, id=project_id)

    try:
        aao  = AvisAppelOffre.objects.get(appel_offre=appel_offre)
        rpao = RPAO.objects.get(appel_offre=appel_offre)
        ccap = CCAP.objects.get(appel_offre=appel_offre)
        bpu_dqe = BPU_DQE.objects.filter(appel_offre=appel_offre)
    except AvisAppelOffre.DoesNotExist:
        aao = None

    # Convertir le logo en base64 avant de passer au template
    logo_base64 = get_image_base64(appel_offre.logo)

    context = {
        'appel_offre': appel_offre,
        'aao':         aao,
        'rpao':        rpao,
        'ccap':        ccap,
        'bpu_dqe' : bpu_dqe,
        'logo_base64': logo_base64,  # ← base64 ou None si pas de logo
    }

    template = loader.get_template('app_travaux/dao_travaux.html')
    html = template.render(context)

    config = pdfkit.configuration(
        wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    ) 
    options = {
        'encoding': 'UTF-8',
        'enable-local-file-access': '',
        'quiet': '',
    }

    # ✅ Écrire dans un fichier temporaire évite le problème de décodage stdout
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
        tmp_path = tmp.name

    try:
        pdfkit.from_string(html, tmp_path, configuration=config, options=options)

        with open(tmp_path, 'rb') as f:
            pdf = f.read()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)  # nettoyage systématique

    nom_fichier = f"appel_offre_{appel_offre.numero_dossier or project_id}.pdf"
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'{mode}; filename="{nom_fichier}"'

    return response

def apercu_marche_travaux(request, project_id):
    return generer_pdf(request, project_id, mode='inline')


def telecharger_marche_travaux(request, project_id):
    return generer_pdf(request, project_id, mode='attachment')