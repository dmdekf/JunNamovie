from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
<<<<<<< HEAD

    def get_score(self):
        return round(self.score.aggregate(model))

=======
    age = models.IntegerField()
    gender = models.BooleanField()
>>>>>>> 4a3b79c5104ad01173dcf9e4229b8a3b27a246d5
    like_movie_genre = models.IntegerField()
