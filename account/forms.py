from django import forms
from .models import User 
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class RegisterForm(forms.ModelForm):
    """ Formulaire d'inscription """

    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")
    phone_number = forms.CharField(max_length=17, widget=PhoneNumberPrefixWidget(
        attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Numéro de téléphone'
        },  
    ))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "company"] 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déja utilisé")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data
    

class LoginForm(forms.Form):
    """Formulaire de connexion"""
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")