from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_title = models.CharField(max_length=45)
<<<<<<< HEAD
    user = models.ForeignKey(get_user_model(),
                             ondelete=models.CASCADE)
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
>>>>>>> 4a3b79c5104ad01173dcf9e4229b8a3b27a246d5


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
<<<<<<< HEAD
    user = models.ForeignKey(get_user_model(),
                             ondelete=models.CASCADE)
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
>>>>>>> 4a3b79c5104ad01173dcf9e4229b8a3b27a246d5
