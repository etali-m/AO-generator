from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Modèle d'utilisateur personnalisé basé sur email"""
     
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField()
    company = models.CharField(max_length=255, blank=True, null=True)
    #country = CountryField(blank_label="Sélectionnez un pays")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email