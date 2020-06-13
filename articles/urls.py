from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "articles"

router = routers.DefaultRouter()

router.register(r'comments', views.CommentViewset)
router.register(r'articlelist', views.ArticleListViewset)

urlpatterns = [
    path('create/', views.create),
    # path('update/<int:article_pk>', views.update, name="update"),
    path('<int:article_pk>', views.article_detail),
    # path('delete/<int:article_pk>', views.delete, name="delete"),
    url(r'^api/', include((router.urls, app_name))),
]
