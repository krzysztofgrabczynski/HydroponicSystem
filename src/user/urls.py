from django.urls import path

from src.user import views as user_views


urlpatterns = [
    path("sign-up/", user_views.UserCreateView.as_view()),
    path("login/", user_views.LoginView.as_view()),
    path("logout/", user_views.LogoutView.as_view()),
]
