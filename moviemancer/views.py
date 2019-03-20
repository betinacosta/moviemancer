# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response

from moviemancer.models import Movie, Viwer
from moviemancer.serializers import MovieSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from moviemancer.helpers import Helpers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
import json
from django.template import RequestContext
from moviemancer.database_handlers import DataBaseHandler
from moviemancer.recommendation import Recommendation


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

def profile(request):
    return render(request,'recommendation/partials/profile.html')

def search(request):
    return render(request,'recommendation/partials/search.html')

def notfound(request):
    return render(request,'recommendation/partials/notfound.html')

def handler404(request):
    response = render_to_response('recommendation/partials/notfound.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response

@csrf_exempt
def get_recommendation(request):

    if request.body:
        request_reco = json.loads(request.body)
        request_user_id = request_reco[u'user_id']

        recommendation_list = json.dumps(Helpers.get_recommendation_list(request_user_id, 1))
        return HttpResponse(recommendation_list)
    else:
        return HttpResponse("Error while loading recommendations")

@csrf_exempt
def update_user(request):
    if request.body:
        request_profile = json.loads(request.body)
        request_user_id = request_profile[u'user_id']
        request_email = request_profile[u'email']
        request_name = request_profile[u'name']
        request_password = request_profile[u'password']

        DataBaseHandler.update_user_info(request_user_id, request_email, request_name, request_password)
        return HttpResponse('Success')
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_all_comments(request):
    if request.body:
        request_comments = json.loads(request.body)
        request_movie_tmdb_id = request_comments[u'tmdb_movie_id']

        all_comments = json.dumps(Helpers.get_comments(request_movie_tmdb_id))
        return HttpResponse(all_comments)
    else:
        return HttpResponse("Erroa o carregar comentarios")

@csrf_exempt
def add_new_comment(request):
    if request.body:
        request_comments = json.loads(request.body)
        request_movie_tmdb_id = request_comments[u'tmdb_movie_id']
        request_user_id = request_comments[u'user_id']
        request_comment = request_comments[u'comment']

        DataBaseHandler.add_comment(request_movie_tmdb_id, request_user_id, request_comment)
        return HttpResponse('Success')
    else:
        return HttpResponse("Erro ao criar comentario")

@csrf_exempt
def delete_user_comment(request):
    if request.body:
        request_comments = json.loads(request.body)
        request_comment_id = request_comments[u'comment_id']

        if DataBaseHandler.delete_comment(request_comment_id):
            return HttpResponse("Success")
        else:
            return HttpResponseServerError("Erro ao deletar comentario")
    else:
        return HttpResponseServerError("Erro ao deletar comentario")

@csrf_exempt
def ratemovie(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_movie_id = request_user_rating[u'movie_id']
        request_rate_id = request_user_rating[u'rate_id']

        DataBaseHandler.rate_movie (request_user_id, request_movie_id, request_rate_id)
        Recommendation.create_user_recommendation(request_user_id)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def rate_first_movies_request(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_movie_id = request_user_rating[u'movie_id']
        request_rate_id = request_user_rating[u'rate_id']

        DataBaseHandler.rate_movie (request_user_id, request_movie_id, request_rate_id)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_auth(request):
    if request.body:
        request_auth = json.loads(request.body)
        request_email = request_auth[u'email']
        request_password = request_auth[u'password']

        if DataBaseHandler.authenticate_user(request_email, request_password):

            user_id = Helpers.get_user_id_by_email(request_email)
            user_data = json.dumps(Helpers.get_user(request_email))
            Recommendation.create_user_recommendation(user_id)

            return HttpResponse(user_data)
        else:
            return HttpResponseServerError('Usuário e Senha não combinam')
    else:
        return HttpResponseServerError('Authentication Failure: No Response Body')

@csrf_exempt
def registration(request):
    if request.body:
        request_register = json.loads(request.body)
        request_name = request_register[u'name']
        request_email = request_register[u'email']
        request_password = request_register[u'password']

        if not Helpers.user_exists(request_email):
            user_id = DataBaseHandler.register_user(request_name, request_email, request_password)
            if user_id:
                return HttpResponse(user_id)
            else:
                return HttpResponseServerError('Erro no cadastro')
    else:
        return HttpResponseServerError('Erro no cadastro')

@csrf_exempt
def validate_user(request):
    if request.body:
        request_validation = json.loads(request.body)
        request_email = request_validation[u'email']

        if not Helpers.user_exists(request_email):
            return HttpResponse('Success')
        else:
            return HttpResponseServerError('User already registered')

@csrf_exempt
def rate_external(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']
        request_rate_id = request_user_rating[u'rate_id']
        request_tmdb_movie_id = request_user_rating[u'tmdb_movie_id']
        request_movie_poster = request_user_rating[u'movie_poster']
        request_movie_title = request_user_rating[u'movie_title']

        if DataBaseHandler.rate_external_movie (request_user_id, request_rate_id, request_tmdb_movie_id, request_movie_poster, request_movie_title):
            Recommendation.create_user_recommendation(request_user_id)
            return HttpResponse('Success')
        else:
            return HttpResponseServerError('Error')
    else:
        return HttpResponseServerError("You are on your own")

@csrf_exempt
def add_watchlist(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        DataBaseHandler.add_to_list(request_user_id, request_movie_id, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    #update recommendation
    Recommendation.create_user_recommendation(request_user_id)

@csrf_exempt
def add_watchlist_external(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_tmdb_movie_id = request_data[u'tmdb_movie_id']
        request_movie_poster = request_data[u'movie_poster']
        request_movie_title = request_data[u'movie_title']

        DataBaseHandler.add_to_list_external(request_user_id, request_tmdb_movie_id, request_movie_poster, request_movie_title, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_watched_list(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']

        user_watchedlist = json.dumps(Helpers.get_watchedlist(request_user_id))
        return HttpResponse(user_watchedlist)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def remove_from_watched_list(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        DataBaseHandler.remove_watched(request_user_id, request_movie_id, 3)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")
    #update recommendation
    Recommendation.create_user_recommendation(request_user_id)

@csrf_exempt
def remove_from_watchlist(request):
    if request.body:
        request_data = json.loads(request.body)
        request_user_id = request_data[u'user_id']
        request_movie_id = request_data[u'movie_id']

        DataBaseHandler.remove_movie_from_list(request_user_id, request_movie_id, 2)
        return HttpResponse(request.body)
    else:
        return HttpResponse("You are on your own")

@csrf_exempt
def get_watch_list(request):
    if request.body:
        request_user_rating = json.loads(request.body)
        request_user_id = request_user_rating[u'user_id']

        user_watchlist = json.dumps(Helpers.get_watchlist(request_user_id))
        return HttpResponse(user_watchlist)
    else:
        return HttpResponse("You are on your own")

def get_rated(request):
    rated_movies = json.dumps(Helpers.get_rated_movies())
    print(rated_movies)
    return HttpResponse(rated_movies)

@csrf_exempt
def filter_reco(request):
    if request.body:
        request_filter = json.loads(request.body)
        request_user_id = request_filter[u'user_id']
        request_minYear = request_filter[u'minYear']
        request_maxYear = request_filter[u'maxYear']
        request_minRuntime = request_filter[u'minRuntime']
        request_maxRuntime = request_filter[u'maxRuntime']
        request_language = request_filter[u'language']
        request_genres = request_filter[u'genres']

        filtered = json.dumps(Recommendation.filter_recommendation(request_genres, request_minYear, request_maxYear, request_minRuntime, request_maxRuntime, request_language, request_user_id))
        return HttpResponse(filtered)
    else:
        return HttpResponseServerError("You are on your own")


class MovieView(generics.ListAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

