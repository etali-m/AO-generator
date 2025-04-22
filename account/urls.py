from django.urls import path
from .views import *

urlpatterns = [
    path('register', register_view, name="register"), 
    path('login', login_view, name="login"),

    path('api/signup/', api_registerView.as_view(), name="signup"),
    path('api/verify-email/', VerifyUserEmail.as_view(), name='verify'),
    path('api/login/', LoginUserView.as_view(), name='login'),
    path('api/profil/', UserProfilView.as_view(), name='profil'),
    path('api/password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('api/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('api/set-new-password/', SetNewPassword.as_view(), name='set-new-password'),
    path('api/logout/', LogoutUserView.as_view(), name='logout')
]