from django.contrib.auth.models import BaseUserManager 

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, phone_number, company, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        
        # Validation des champs obligatoires
        if not first_name:
            raise ValueError(_("The first_name is required"))
        if not phone_number:
            raise ValueError(_("Phone number is required"))  
        
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number, 
            company=company,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Créer un super utilisateur avec tous les privilèges"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True) 
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Un superutilisateur doit avoir is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Un superutilisateur doit avoir is_superuser=True")

        return self.create_user(email, password, **extra_fields)
