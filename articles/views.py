from django.shortcuts import render, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    # @action(detail=True, methods=['post'])
    # def create(self, request, pk=None):


class ArticleDetailViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def create(request):
    pass


def update(request, article_pk):
    pass


def article_detail(request, article_pk):
    pass


def delete(request, article_pk):
    pass
