from django.shortcuts import render

from recommendation.models import Movie, User
from recommendation.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from recommendation.queries import movie_by_user_list
 

def index(request):
    return render(request,'recommendation/home.html')

class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RecoView (generics.ListAPIView):
    model = Movie
    # Fix queryset
    queryset = movie_by_user_list(1, 'recommendation')
    serializer_class = MovieSerializer

def main(request):
    return render(request,'recommendation/partials/main.html')