"""URL patterns for accounts app"""
from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    #Include default auth url
    path("", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
]