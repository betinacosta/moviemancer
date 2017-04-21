from django.shortcuts import render

from recommendation.models import Movie, User
from recommendation.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from recommendation.queries import movie_by_user_list, rate_movie
from recommendation.reco import add_recommentation_to_database, add_to_list, add_to_list_external
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

def moviedetails(request):
    return render(request,'recommendation/partials/moviedetails.html')

@csrf_exempt
def ratemovie(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_movie_id = request_user_rating[u'movie_id']
        request_rate_id = request_user_rating[u'rate_id']

        rate_movie (request_user_id, request_movie_id, request_rate_id)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    
    #update recommendation
    add_recommentation_to_database(1)

@csrf_exempt
def add_watchlist(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        add_to_list(request_user_id, request_movie_id, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    #update recommendation
    add_recommentation_to_database(1)

@csrf_exempt
def add_watchlist_external(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_tmdb_movie_id = request_data[u'tmdb_movie_id']
        request_movie_poster = request_data[u'movie_poster']
        request_movie_title = request_data[u'movie_title']

        add_to_list_external(request_user_id, request_tmdb_movie_id, request_movie_poster, request_movie_title, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RecoView (generics.ListAPIView):
    model = Movie
    add_recommentation_to_database(1)
    queryset = movie_by_user_list(1, 'recommendation')
    serializer_class = MovieSerializer

