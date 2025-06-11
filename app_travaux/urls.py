from django.urls import path     
from .views import *

urlpatterns = [
    path('<int:project_id>/aao', AAOView.as_view(), name="aao-travaux"),
]