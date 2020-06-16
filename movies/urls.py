from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url, include

app_name = 'movies'

router = routers.DefaultRouter()
# router.register(r'articlelist', views.ArticleListViewset)
# router.register(r'comments', views.CommentViewset)

# urlpatterns = [
#     # path('create/', views.create, name="create"),
#     # path('update/<int:article_pk>', views.update, name="update"),
#     # path('<int:article_pk>', views.article_detail, name="article_detail"),
#     # path('delete/<int:article_pk>', views.delete, name="delete"),
# ]


urlpatterns = [
    path('', views.index, name='index'),

    path('movies/<int:pk>/', views.movies_view, name="movies_view"),
    path('api/movies/', views.movies_list, name="movies_list"),
    path('api/genres/', views.genres_list, name="genres_list"),
    path('api/genres/<int:pk>/', views.genres_detail, name="genres_detail"),

    path('api/movies/<int:pk>/score/', views.input_score, name="input_score"),

    url(r'^api/', include((router.urls, app_name)))
]
