from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
import csv
# Create your models here.


class Genre(models.Model):
    type = models.CharField(max_length=150)

    # def __str__(self):
    #     return self.type


class Movie(models.Model):
    title = models.CharField(max_length=150)
    popularity = models.IntegerField(default=0)
    release = models.DateField(blank=True)
    poster_URL = models.URLField(max_length=200, default='', blank=True)
    backdrop_URL = models.URLField(max_length=200, default='', blank=True)
    adult = models.BooleanField()
    overview = models.TextField()
    runtime = models.IntegerField(default=0)
    status = models.BooleanField()
    tagline = models.CharField(max_length=200)
    vote_aver = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title


class Score(models.Model):
    score = models.FloatField(blank=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='movie_scores')
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='score_movie')

    # def get_movieid(self):
    #     return self.movie.id


class recommend(models.Model):
    like_movie_genre = models.CharField(max_length=45)
    recommend_genre = models.ManyToManyField(Genre, related_name='recommends')
