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
    path('<int:article_pk>/', views.detail, name="detail"),
    # path('api/article_create/', views.create),
    # path('update/<int:article_pk>', views.update, name="update"),
    path('api/article/<int:article_pk>/', views.article_detail),
    # path('delete/<int:article_pk>', views.delete, name="delete"),
    url(r'^api/', include((router.urls, app_name))),
]
