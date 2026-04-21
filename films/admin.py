from django.contrib import admin
from .models import Film, Categorie # existent dans models.py
# Register your models here.
admin.site.register(Categorie)
admin.site.register(Film)
