from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, ChangePasswordView, ForgotPasswordVies, ForgotPasswordCompleteVies, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view() ),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_pas/', ChangePasswordView.as_view()),
    path('forgot_email/', ForgotPasswordVies.as_view()),
    path('forgot_active/', ForgotPasswordCompleteVies.as_view())
]