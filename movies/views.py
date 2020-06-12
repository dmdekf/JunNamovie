from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(request):
<<<<<<< HEAD
    return render(request, 'movies/index.html')
=======
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
>>>>>>> 4a3b79c5104ad01173dcf9e4229b8a3b27a246d5
