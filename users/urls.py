from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileUpdateView, generate_new_password, VerificationView, ErrorVerification

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', VerificationView.as_view(), name='verification'),
    path('verification/error/', ErrorVerification.as_view(), name='verify_email_error'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
]