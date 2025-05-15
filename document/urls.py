from django.urls import path
from .views import home_view, createProject_view, typeMarcheView, AppelOffreView

urlpatterns = [
    path('', home_view, name="home"),  
    path('create/<int:pk>', createProject_view, name="create-project"),

    path('api/type-marche', typeMarcheView.as_view(), name="type-marche"),
    path('api/appel-offre', AppelOffreView.as_view(), name="appel-offre")
]