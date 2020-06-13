from django.shortcuts import render, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment

from rest_framework import viewsets
# Create your views here.


class ArticleListViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def create(request):
    pass


def update(request, article_pk):
    pass


def article_detail(request, article_pk):
    pass


def delete(request, article_pk):
    pass
