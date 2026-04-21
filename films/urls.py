from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path("", views.index, name="film_index"), 
    path("<int:film_id>/", views.detail, name="film_detail"),
]