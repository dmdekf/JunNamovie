from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = "articles"

router = routers.DefaultRouter()

router.register(r'comments', views.CommentViewset)
router.register(r'articlelist', views.ArticleListViewset)

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:article_pk>/commentcreate/',
         views.commentCreate, name="commentCreate"),
    url(r'^api/', include((router.urls, app_name))),
]
