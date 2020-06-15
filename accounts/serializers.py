from .models import User
from rest_framework import serializers
from movies.serializers import ScoreSerializer


class UserSerializer(serializers.ModelSerializer):
    score_movie = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'score_movie')
