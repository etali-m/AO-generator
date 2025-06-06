from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import send_normal_mail
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import get_user_model

from .models import User

#Serializer pour l'enregistrement d'un utilisateur
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True) #les mots de passe ne seront par retourner après l'enregistrement de l'utilisateur
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'company', 'password', 'password2']

    def validate_email(self, value):
        User = get_user_model()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2') 

        if password != password2:
            raise serializers.ValidationError("Les mots de passe de correspondent pas")
        
        return attrs
    
    #fonction pour créer une nouvelle instance du modèle User Elle est appelée lorsque des données valides sont passées au sérialiseur pour créer une nouvelle instance.
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            phone_number = validated_data.get('phone_number'),
            company = validated_data.get('company'),
            password = validated_data.get('password')
        )
        return user


#Sérializer pour récuperer les infos sur un utilisateur.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number',  'company']


#serializer pour la connextion d'un utitilisateur
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True) 
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password' , 'access_token', 'refresh_token']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Identifiants incorrects")
        #on s'assure que l'adresse email de l'utilisateur est vérifiée avant de le connecter
        if not user.is_verified:
            raise AuthenticationFailed("Cette adresse email n'est pas vérifiée")
        
        #générer un token pour l'utilisateur à partir de la fonction tokens() du modèle User
        user_tokens = user.tokens()

        return {
            'email' : user.email, 
            'access_token' : str(user_tokens.get('access')),
            'refresh_token' : str(user_tokens.get('refresh'))
        }

#serializer pour la requête de changement de mot de passe que l'utilisateur envoie
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields=['email']

    def validate(self, attrs):
        email = attrs.get('email')

        #si l'utilisateur existe on lui envoi un mail avec un line pour le permettre de changer son mot de passe
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id)) #encoder l'identifiant de l'utilisateur
            token = PasswordResetTokenGenerator().make_token(user) #générer un token pour la modification de mot de passe par l'utilisateur
            request = self.context.get('request')
            site_domain = get_current_site(request).domain
            relative_link = reverse('password-reset-confirm', kwargs={'uidb64':uidb64, 'token': token})
            abslink = f"http://{site_domain}{relative_link}" 
            email_body = f"Hi use the link below to reset you password \n {abslink}"
            data = {
                'email_body': email_body,
                'email_subject': "Reset your password",
                'to_email': user.email
            }

            send_normal_mail(data)
        return super().validate(attrs)


#Serializer pour envoyer les données du nouveau mot de passe
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    uidb64 = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True) #token pour la modification de mot de passe

    class Meta:
        fields = ['password', 'confirm_password', 'uidb64', 'token']

    def validate(self, attrs):
        try: 
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')

            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("reset link is invalid or has expired", 401)
            if password != confirm_password:
                raise AuthenticationFailed("password do not match")
            
            user.set_password(password)
            user.save()

            return user
        except Exception as e:
            return AuthenticationFailed("link is invalide or has expired")

#Serializer pour la déconnexion
class LogoutUserSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or has expired') 
    }

    def validate(self, attrs):
        self.token = attrs.get('refresh_token')

        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            return self.fail('bad_token')
