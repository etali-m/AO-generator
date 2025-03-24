from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Modèle d'utilisateur personnalisé basé sur email"""
     
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    company = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "country"]

    def __str__(self):
        return self.email