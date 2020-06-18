from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Genre, Movie, Score
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ScoreForm
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, ScoreSerializer
from django.db.models import Sum, Count, Avg
from django.contrib import messages
# Create your views here.


class MovieListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres
    }
    return render(request, 'movies/index.html', context)


def genres_view(request):
    genre = get_object_or_404(Genre, type=request.GET.get('type'))
    return render(request, 'movies/genre.html', {'genre': genre})


@api_view(["GET"])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def genres_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)


@api_view(["GET"])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def movies_view(request, pk):
    form = ScoreForm()
    movie = get_object_or_404(Movie, pk=pk)

    scoreAVG = Score.objects.filter(movie=pk).aggregate(Avg('score'))
    scoreCount = Score.objects.filter(movie=pk).aggregate(Count('score'))
    context = {
        'movie': movie,
        'form': form,
        'scoreAVG': round(scoreAVG['score__avg'], 1),
        'scoreCount': scoreCount['score__count']
    }
    return render(request, 'movies/movie_detail.html', context)


@api_view(["GET"])
def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


def inputScore(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.movie = movie
            score.save()
            messages.info(request, '점수가 등록되었습니다.')
            return redirect('movies:movies_view', movie_pk)
    else:
        messages.warning(request, '점수 등록을 위해서는 로그인이 필요합니다.')
        return redirect('accounts:login')
