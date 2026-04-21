from django.contrib import admin
from django.urls import path
from acteurs import views

urlpatterns = [ 
    path("ajoutActeur/", views.ajoutActeur, name="ahoutActeur"), # <-- Ajoute le slash ici
]