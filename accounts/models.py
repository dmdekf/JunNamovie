from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    age = models.IntegerField()
    gender = models.BooleanField()

    def get_score(self):
        return round(self.score.aggregate(model))

    like_movie_genre = models.IntegerField()
