from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(ArticleListSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta(ArticleListSerializer.Meta):
        fields = '__all__'
