from rest_framework import serializers
from recommendation.models import Movie, Type, MovieList, List
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'tmdb_movie_id')