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
                             on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE, related_name='article_comments')
