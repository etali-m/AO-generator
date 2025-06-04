from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, get_object_or_404
from .models import TypeMarche, AppelOffre, Piece, StatutPiece
from .serializers import TypeMarcheSerializer, AppelOffreSerializer, PieceSerializer, StatutPieceSerializer

# Create your views here.
def home_view(request): 
    # Récupérer les 4 derniers objets TypeMarche
    top_type = TypeMarche.objects.all()[:4]

    # Récupérer les autres objets TypeMarche en excluant les 4 premiers
    others_type = TypeMarche.objects.all().exclude(id__in=top_type.values_list('id', flat=True))

    # Passer les objets au contexte du template
    context = {
        'top_type': top_type,
        'others_type': others_type,
    }

    return render(request, "document/home.html", context)

#Création d'un dossier d'appel d'offre
def createProject_view(request, pk):
    type_marche = get_object_or_404(TypeMarche, pk=pk)

    context = {
        'type_marche': type_marche,
    }
    return render(request, "document/new_project.html", context)


class typeMarcheView(GenericAPIView): 
    serializer_class = TypeMarcheSerializer
    queryset = TypeMarche.objects.all()

    def get(self, request): 
        type = request.GET.get('slug')

        queryset = self.get_queryset() #recupération de la requete
        
        if type:
            queryset = queryset.filter(slug=type)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PieceView(GenericAPIView):
    serializer_class = PieceSerializer
    queryset = Piece.objects.all()

    #renvoi toutes le pièces disponible pour le type du dossier d'appel d'offre
    def get(self, request, *args, **kwargs):
        type_id = kwargs.get('type_id')
        queryset = self.get_queryset().filter(type_marche=type_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class StatuPieceView(ListAPIView):
    serializer_class = StatutPieceSerializer

    def get_queryset(self):
        id_projet = self.kwargs.get('project_id')
        print(id_projet)
        print(StatutPiece.objects.filter(appel_offre__id=id_projet))
        return StatutPiece.objects.filter(appel_offre__id=id_projet)


class AppelOffreView(GenericAPIView):
    serializer_class = AppelOffreSerializer
    queryset = AppelOffre.objects.all() 

    def get(self, request, *args, **kwargs):
        user = request.user  
        queryset = self.get_queryset().filter(user=user) #recupérer les DAO créer par l'utilisateur connecté
        dossier = self.request.GET.get('dossier') #recupérer le DAO que l'utilisateur a selectionner
        if dossier: 
            queryset = queryset.filter(id=dossier) 
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()  #recupérer les données envoyé depuis le frontend
        data['user'] = request.user.id #on ajoute user à l'objet data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'data': serializer.data,
            'message': "Le Dossier d'Appel d'offre a été créé avec succès."
        }, status=status.HTTP_201_CREATED)