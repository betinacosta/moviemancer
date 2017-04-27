from django.shortcuts import render

from recommendation.models import Movie, User
from recommendation.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from recommendation.queries import movie_by_user_list, rate_movie, get_watchedlist, remove_watched, get_watchlist, remove_movie_from_list, authenticate_user, get_user,jsonify_reco_list, get_user_by_email
from recommendation.reco import add_recommentation_to_database, add_to_list, add_to_list_external, rate_external_movie
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    return render(request,'recommendation/home.html')

def moviemancer(request):
    return render(request,'recommendation/partials/moviemancer.html')

def recommendation(request):
    return render(request,'recommendation/partials/recommendation.html')

def moviedetails(request):
    return render(request,'recommendation/partials/moviedetails.html')

def show_watched_list(request):
    return render(request,'recommendation/partials/watchedlist.html')

def show_watchlist(request):
    return render(request,'recommendation/partials/watchlist.html')

def show_filters(request):
    return render(request,'recommendation/partials/filters.html')

def show_login(request):
    return render(request,'recommendation/login.html')

def show_singup(request):
    return render(request,'recommendation/singup.html')

def register_genres(request):
    return render(request,'recommendation/registergenres.html')

@csrf_exempt
def get_recommendation(request):
    if request.body:
        request_reco = json.loads(request.body)
        request_user_id = request_reco[u'user_id']

        recommendation_list = jsonify_reco_list(request_user_id, 'recommendation')
        return HttpResponse(recommendation_list)
    else:
        return HttpResponse("You are on your own")        

@csrf_exempt
def ratemovie(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_movie_id = request_user_rating[u'movie_id']
        request_rate_id = request_user_rating[u'rate_id']

        rate_movie (request_user_id, request_movie_id, request_rate_id)
        add_recommentation_to_database(request_user_id)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_auth(request):
    if request.body:
        request_auth = json.loads(request.body)
        request_email = request_auth[u'email']
        request_password = request_auth[u'password']

        print('email', request_email, ' Senha: ', request_password)

        if authenticate_user(request_email, request_password):
            user_id = get_user_by_email(request_email)
            add_recommentation_to_database(user_id)
            user_data = get_user(request_email)
            return HttpResponse(user_data)
        else:
            return HttpResponse('Erro')
    else:
        return HttpResponse('Authentication Failure: No Response Body')

def registration(request):
    pass

@csrf_exempt
def rate_external(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_rate_id = request_user_rating[u'rate_id']
        request_tmdb_movie_id = request_user_rating[u'tmdb_movie_id']
        request_movie_poster = request_user_rating[u'movie_poster']
        request_movie_title = request_user_rating[u'movie_title']

        rate_external_movie (request_user_id, request_rate_id, request_tmdb_movie_id, request_movie_poster, request_movie_title)
        add_recommentation_to_database(request_user_id)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

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
    add_recommentation_to_database(request_user_id)

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

@csrf_exempt
def get_watched_list(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        
        user_watchedlist = get_watchedlist(request_user_id)
        return HttpResponse(user_watchedlist)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def remove_from_watched_list(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        remove_watched(request_user_id, request_movie_id, 3)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    #update recommendation
    add_recommentation_to_database(request_user_id)

@csrf_exempt
def remove_from_watchlist(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        remove_movie_from_list(request_user_id, request_movie_id, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_watch_list(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        
        user_watchlist = get_watchlist(request_user_id)
        return HttpResponse(user_watchlist)
    else:
        return HttpResponse("You are on your own")

class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

