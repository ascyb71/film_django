from django.contrib import admin
from .models import Film, Categorie # existent dans models.py
# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display=("id","nom")

class FilmAdmin(admin.ModelAdmin):

    list_display=("id","title","date_sortie","qte_stock","prix_location","date_creation","date_creation")
    search_field=("id","title")
    fields=("title","date_sortie","qte_stock","prix_location")
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Film,FilmAdmin)


