from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url, include

app_name = 'movies'

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name='index'),

    path('movies/<int:pk>/', views.movies_view, name="movies_view"),
    path('api/movies/', views.movies_list, name="movies_list"),
    path('api/genres/', views.genres_list, name="genres_list"),
    path('api/genres/<int:pk>/', views.genres_detail, name="genres_detail"),

    url(r'^api/', include((router.urls, app_name))),
    path('movies/<int:movie_pk>/inputScore/',
         views.inputScore, name="inputScore"), ]
