from django.urls import path     
from .views import *

urlpatterns = [
    path('edit/<int:pk>', home_travaux, name="home-travaux"),
    path('edit/<int:id_projet>/aao', aao_travaux, name="aao-travaux"),
]