from django.shortcuts import render

# Create your views here.
def home_travaux(request, pk):
    return render(request, "app_travaux/home.html")


def aao_travaux(request, id_projet):
    return render(request, "app_travaux/aao.html")