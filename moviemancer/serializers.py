from rest_framework import serializers
from moviemancer.models import Movie, Type, MovieList, List, Viwer, Rating
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'tmdb_movie_id', 'tmdb_poster', 'tmdb_title')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viwer
        fields = ('user_id',)