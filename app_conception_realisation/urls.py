from django.urls import path
from .views import *

urlpatterns = [
    path('<int:project_id>/aao', AAOView.as_view(), name="aao-cr"),
    path('<int:project_id>/rpao', RPAOView.as_view(), name="rpao-cr"),
    path('<int:project_id>/grille_notation', GrilleNotationView.as_view(), name="grille_notation-cr"),
    path('<int:project_id>/ccap', CCAPView.as_view(), name="ccap-cr"),
    path('<int:project_id>/tdr', TDRView.as_view(), name="tdr-cr"),
    path('<int:project_id>/cctp', CCTPView.as_view(), name="cctp-cr"),
    path('<int:project_id>/bpu_dqe', BPU_DQEView.as_view(), name="bpu_dqe-cr"),
    path('<int:project_id>/modele_marche', ModelMarcheView.as_view(), name="modele-marche-cr"),
    path('<int:project_id>/telecharger', telecharger_marche_conception_realisation, name="telecharger-cr"),
    path('<int:project_id>/apercu/', apercu_marche_conception_realisation, name='apercu_pdf-cr'),
]
