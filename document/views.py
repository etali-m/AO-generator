from django.shortcuts import render, get_object_or_404
from .models import TypeMarche

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


def createProject_view(request, pk):
    type_marche = get_object_or_404(TypeMarche, pk=pk)

    context = {
        'type_marche': type_marche,
    }
    return render(request, "document/new_project.html", context)