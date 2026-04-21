from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from films.models import Film

# Create your views here.
def index(request):
    # 1. Get the search term from the URL
    query = request.GET.get('search')
    
    # 2. Check if the user typed something
    if query:
        # Filter movies where the title contains the search term (case-insensitive)
        films = Film.objects.filter(title__icontains=query)
    else:
        # If no search, show all movies
        films = Film.objects.all()
        
    context = {"films": films}
    return render(request, 'index.html', context)

def detail(request, film_id):
    # film = Film.objects.get(id=film_id) # The simple way
    film = get_object_or_404(Film, id=film_id) # The safe way (handles 404)
    return render(request, "detail.html", {"film": film})