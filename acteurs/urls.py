from django.contrib import admin
from django.urls import path
from acteurs import views

urlpatterns = [ 

    path("ajoutActeur/", views.ajoutActeur, name="ahoutActeur"),
    path("editActeur/<int:acteur_id>", views.editActeur),
    path("deleteActeur/<int:acteur_id>", views.deleteActeur),

]