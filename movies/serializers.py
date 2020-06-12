from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Movie, Score, Recommend


class ScoreSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = Score
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    movie_scores = ScoreSerializer(many=True, read_only=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"
