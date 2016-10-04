from rest_framework import serializers
from recommendation.models import Movie
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'tmdb_movie_id')