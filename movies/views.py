from .models import Movie
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Score
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, ScoreSerializer
import json
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


@api_view(["GET", "POST"])
def input_score(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        scores = movie.scores.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            request.data["movie"] = movie.id
            request.data["user"] = request.user.id
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def movies_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

    # item number per page
    num_page = 10
    paginator = Paginator(data, num_page)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'brand/basic.html', context={'catid': catid, 'contacts': contacts})

