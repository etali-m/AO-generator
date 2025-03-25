from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
def register_view(request):
    """Vue pour l'inscription d'un utilisateur"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect("login")
        else:
            print(form.errors)  # Debugging : affiche les erreurs dans la console
    else:
        form = RegisterForm()
    
    return render(request, "account/register.html", {"form": form})


def login_view(request):
    """Vue pour la connexion d'un utilisateur"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password) 

            if user:
                login(request, user)
                messages.success(request, "Connexion réussie")
                return redirect('document/home.html')
            else: 
                form.add_error(None, "Email ou mot de passe incorrect")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})