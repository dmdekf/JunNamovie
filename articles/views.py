from django.shortcuts import render, get_object_or_404, redirect
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .forms import CommentForm
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# def perform_create(self, serializer):
#     serializer.save()
#     return Response(serializer.data)


class CommentViewset(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleListViewset(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('-pk')
    serializer_class = ArticleListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


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
                return Response(serializer.data)


@require_POST
@login_required
def comment_create(request, article_pk):
    review = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    return redirect('articles:index', article.pk)


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


요걸 살려서 붙여놓고 감니다~~~


def inputScore(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.movie = movie
            score.save()
        return redirect('movies:index')
    else:
        messages.warning(request, '댓글 작성을 위해서는 로그인이 필요합니다.')
        return redirect('accounts:login')
