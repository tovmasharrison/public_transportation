from django.urls import path, include

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path("edit/", views.EditView.as_view(), name="edit"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("delete/", views.DeleteUser.as_view(), name="delete"),
    path("", include("django.contrib.auth.urls")),
]