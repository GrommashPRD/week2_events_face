from django.urls import path

from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path("api/auth/register/", RegisterView.as_view(), name="register-user"),
    path("api/auth/login/", LoginView.as_view(), name="login-user"),
    path("api/auth/logout/", LogoutView.as_view(), name="logout-user"),
]
