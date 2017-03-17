from django.shortcuts import render

from recommendation.models import Movie, User
from recommendation.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from recommendation.queries import movie_by_user_list, rate_movie, remove_movie_from_list, add_to_watched_list
from recommendation.reco import add_recommentation_to_database
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    return render(request,'recommendation/home.html')

def main(request):
    return render(request,'recommendation/partials/main.html')

def fullreco(request):
    return render(request,'recommendation/partials/full-recommendation.html')

@csrf_exempt
def recoratemovie(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_movie_id = request_user_rating[u'movie_id']
        request_rate_id = request_user_rating[u'rate_id']

        #Add user rate to movie
        rate_movie(request_user_id, request_movie_id, request_rate_id)
        #Removes movie from recommended list (id = 1)
        remove_movie_from_list(request_user_id, request_movie_id)
        #Add movie to user's watched list
        add_to_watched_list(request_user_id, request_movie_id)

        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    
    #update recommendation
    add_recommentation_to_database(1)

class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RecoView (generics.ListAPIView):
    model = Movie
    add_recommentation_to_database(1)
    queryset = movie_by_user_list(1, 'recommendation')
    serializer_class = MovieSerializer

