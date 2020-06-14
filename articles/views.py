from django.shortcuts import render, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
# Create your views here.


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)  # NOT NULL CONSTRAINT FAILED
        return Response(serializer.data)


def index(request):
    return render(request, 'articles/index.html')


def article_detail(request, article_pk):
    pass


def delete(request, article_pk):
    pass
