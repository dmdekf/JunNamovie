from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    age = models.IntegerField()
    gender = models.BooleanField()
    like_movie_genre = models.IntegerField()
