from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

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
  