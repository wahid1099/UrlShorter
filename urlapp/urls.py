from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.createShortURL, name="create"),
    path("<str:url>", views.redirect, name="redirect"),

]
