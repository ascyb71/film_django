from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from films.models import Film

# Create your views here.
def index(request):
    films = Film.objects.all()
    context = {"films": films}
    # Enlève "films/" avant "index.html"
    return render(request, 'index.html', context)

def detail(request, film_id):
    # film = Film.objects.get(id=film_id) # The simple way
    film = get_object_or_404(Film, id=film_id) # The safe way (handles 404)
    return render(request, "films/detail.html", {"film": film})