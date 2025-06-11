from django.urls import path
from .views import typeMarcheView, AppelOffreView, StatuPieceView

urlpatterns = [ 
    path('type-marche', typeMarcheView.as_view(), name="type-marche"),
    path('statutpieces/<int:project_id>', StatuPieceView.as_view(), name="piece"), #récuperer toutes les pieces pour une catégorie de marché.
    path('appel-offre', AppelOffreView.as_view(), name="appel-offre"), #gestion des appels d'offre (Get, Create, Update, Delete)
]