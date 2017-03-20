from rest_framework import serializers
from recommendation.models import Movie, Type, MovieList, List, User, Rating
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'tmdb_movie_id', 'tmdb_poster', 'tmdb_title')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id',)