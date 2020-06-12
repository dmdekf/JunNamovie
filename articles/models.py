from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_title = models.CharField(max_length=45)
    user = models.ForeignKey(get_user_model(),
                             ondelete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),
                             ondelete=models.CASCADE)
