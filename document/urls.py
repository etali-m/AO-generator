from django.urls import path
from .views import typeMarcheView, AppelOffreView, StatuPieceView, StatutPieceUpdateView, AppelOffreDetailView

urlpatterns = [ 
    path('type-marche', typeMarcheView.as_view(), name="type-marche"),
    path('statutpieces/<int:project_id>', StatuPieceView.as_view(), name="piece"), #récuperer toutes les pieces pour une catégorie de marché.
    path('statutpieces/<int:piece_id>/update', StatutPieceUpdateView.as_view(), name="update-statut"),
    path('appel-offre', AppelOffreView.as_view(), name="appel-offre"),  # GET (liste), POST (create)
    path('appel-offre/<int:pk>', AppelOffreDetailView.as_view(), name="appel-offre-detail"),  # PUT/PATCH, DELETE
]

