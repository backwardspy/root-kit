from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /
    path("", views.Index.as_view(), name="index"),
    # ex: /accounts/*
    path("accounts/", include("django.contrib.auth.urls")),
    # ex: /accounts/register
    path("accounts/register/", views.Register.as_view(), name="register"),
]
