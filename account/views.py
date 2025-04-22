from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, OneTimePassword
from .forms import RegisterForm, LoginForm


from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, LoginSerializer, PasswordResetRequestSerializer, SetNewPasswordSerializer, LogoutUserSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from .utils import send_code_to_user

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


""" API VIEWS """
class api_registerView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            #send email function
            send_code_to_user(user['email'])
            return Response({
                'data': user,
                'message': f"hi thanks for siging a passcode have been in your mail"
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#fonction pour vérifier l'utilisateur avec le code otp pour compléter son enregistrement
class VerifyUserEmail(APIView):
    """
    Vue API pour vérifier l'email d'un utilisateur en utilisant un code OTP.

    Cette vue répond aux requêtes POST et vérifie si le code OTP fourni est valide.
    Si le code est valide et que l'utilisateur n'est pas déjà vérifié, l'utilisateur est marqué comme vérifié.

    Args:
        request (Request): L'objet de requête contenant les données POST.

    Returns:
        Response: Une réponse HTTP avec un message et un statut approprié.
    """
    def post(self, request):
        otp_code = request.data.get('otp')
        try:
            user_code_obj = OneTimePassword.objects.get(code=otp_code)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message' : 'account email verify successfully'
                }, status=status.HTTP_200_OK)
            return Response({
                'message': 'code is invalide user already verified'
            }, status=status.HTTP_204_NO_CONTENT)
        
        except OneTimePassword.DoesNotExist:
            return Response({
                'message' : 'passcode not provided'
            }, status=status.HTTP_404_NOT_FOUND)


#fonction de connexion d'un utilisateur avec le token d'accès généré
class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#tester l'authentification d'un utilisateur
class UserProfilView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    #Mise à jour des informations utilisateur
    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Requete de changement de mot de pass
class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        return Response(
            {'message': "A link has been sent to your email to reset your password"}, 
            status = status.HTTP_200_OK
            )

#fonction pour la confirmation du nouveau mot de passe (Cette vue s'affiche lorsque l'utilisateur clique sur lien envoyé par mail) 
class PasswordResetConfirm(GenericAPIView):
    """
        elle est utilisée pour vérifier que le token qui apparait dans l'url générer lors de la requete est toujours valide
    """
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    'message' : 'token is invalid or has expired'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response({'success': True, 'message': 'Credentials is valide', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError:
            return Response({ 'message': 'token is invalid or has expired'}, status=status.HTTP_401_UNAUTHORIED)


#fonction pour changer effectivement le mot de passe
class SetNewPassword(GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'password reset successfully'}, status=status.HTTP_200_OK)
   
    
#fonction de déconnexion
class LogoutUserView(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permissions_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)