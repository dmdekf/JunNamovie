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
    url(r'^api/', include((router.urls, app_name)))
]
