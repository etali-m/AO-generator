from django.urls import path     
from .views import *

urlpatterns = [
    path('<int:project_id>/aao', AAOView.as_view(), name="aao-travaux"),
    path('<int:project_id>/rpao', RPAOView.as_view(), name="rpao-travaux"),
    path('<int:project_id>/ccap', CCAPView.as_view(), name="ccap-travaux"),
    path('<int:project_id>/cctp', CCTPView.as_view(), name="cctp-travaux"),
    path('<int:project_id>/bpu', BPUView.as_view(), name="bpu-travaux"),
    path('<int:project_id>/dqe', DQEView.as_view(), name="dqe-travaux"),
    path('<int:project_id>/modele_marche', ModelMarcheView.as_view(), name="madele-marche-travaux"),
    path('<int:project_id>/telecharger', telecharger_marche_travaux, name="telecharger-travaux"),
]
