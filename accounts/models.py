from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    like_movie_genre = models.IntegerField()

    def __str__(self):
        return self.username
