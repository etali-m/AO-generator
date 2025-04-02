from django.urls import path     
from .views import *

urlpatterns = [
    path('edit_travaux/<int:pk>', home_travaux, name="home-travaux"),
]