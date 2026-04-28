from django.contrib import admin
from .models import Film, Categorie 

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display=("id","nom")

class FilmAdmin(admin.ModelAdmin):
    list_display=("id","title","date_sortie","qte_stock","prix_location","categorie","date_creation")
    search_fields=("id","title")
    fields=("title","date_sortie","prix_location","qte_stock","categorie")

admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Film,FilmAdmin)