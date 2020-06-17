from django.shortcuts import render, get_object_or_404, redirect
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CommentForm
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from .permissions import IsOwnerOrReadOnly


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleListViewset(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('-pk')
    serializer_class = ArticleListSerializer


@api_view(['GET', 'POST'])
def index(request):
    form = CommentForm()
    context = {
        'form': form,
    }
    if request.method == "GET":
        return render(request, 'articles/index.html', context)
    else:
        if request.user.is_authenticated:
            request.data["title"] = title
            request.data["movie_title"] = movie_title
            request.data["content"] = content
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                # NOT NULL CONSTRAINT FAILED
                serializer.save(user=request.user)
                messages.success(request, '글이 작성되었습니다.')
                return Response(serializer.data)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    return render(request, 'articles/detail.html', {'article': article})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


def delete(request, article_pk):
    pass


@require_POST
@login_required
def commentCreate(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
        messages.success(request, '댓글이 등록되었습니다.')
        return redirect('articles:index')
