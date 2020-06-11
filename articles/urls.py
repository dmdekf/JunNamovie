from django.urls import path, include
from . import views

app_name = "articles"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('update/<int:article_pk>', views.update, name="update"),
    path('<int:article_pk>', views.article_detail, name="article_detail"),
    path('delete/<int:article_pk>', views.delete, name="delete"),
]
