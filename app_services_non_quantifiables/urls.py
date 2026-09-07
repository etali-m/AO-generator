from django.urls import path
from .views import *

urlpatterns = [
    path('<int:project_id>/aao', AAOView.as_view(), name="aao-snq"),
    path('<int:project_id>/rpao', RPAOView.as_view(), name="rpao-snq"),
    path('<int:project_id>/ccap', CCAPView.as_view(), name="ccap-snq"),
    path('<int:project_id>/tdr', TDRView.as_view(), name="tdr-snq"),
    path('<int:project_id>/telecharger', telecharger_marche_services_non_quantifiables, name="telecharger-snq"),
    path('<int:project_id>/apercu/', apercu_marche_services_non_quantifiables, name='apercu_pdf-snq'),
]
