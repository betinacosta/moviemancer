# -*- coding: utf-8 -*-
from moviemancer.models import *
import json
import hashlib
import tmdbsimple as tmdb
import time
from decimal import Decimal, ROUND_HALF_UP
from moviemancer.queries import *
from moviemancer.tmdb_handler import TMDbHandler
from moviemancer.helpers import Helpers

class DataBaseHandler:

    def add_movie_to_database(tmdb_id):
        if not Movie.objects.filter(tmdb_movie_id = tmdb_id):
            tmdb_poster = TMDbHandler.get_movie_poster(tmdb_id)
            tmdb_title = TMDbHandler.get_movie_title(tmdb_id)
            tmdb_rating = TMDbHandler.get_tmdb_movie_rating(tmdb_id)
            tmdb_language = TMDbHandler.get_tmdb_movie_language(tmdb_id)
            tmdb_runtime = TMDbHandler.get_tmdb_movie_runtime(tmdb_id)
            tmdb_genres = TMDbHandler.get_tmdb_movie_genres_id(tmdb_id)
            tmdb_year = TMDbHandler.get_tmdb_movie_year(tmdb_id)

            movie_db = Movie(tmdb_movie_id=tmdb_id, tmdb_poster = tmdb_poster, tmdb_title = tmdb_title, tmdb_rating = tmdb_rating, language = tmdb_language, year = tmdb_year, genres = tmdb_genres, runtime = tmdb_runtime)

            try:
                movie_db.save()
                return 'Success'
            except:
                return('Save error')
        return 'Error: movie already exists'

    def add_rating_to_movie(user_id, movie_id, local_rate_id):
        try:
            old_rating = Rating.objects.get(movie_id = movie_id, user_id = user_id)
            new_rating = Rating(rating_id = old_rating.rating_id, user_id = user_id, movie_id = movie_id, rate_id = local_rate_id)
        except Rating.DoesNotExist:
            new_rating = Rating(user_id = user_id, movie_id = movie_id, rate_id = local_rate_id)

        new_rating.save()

    def remove_movie_from_list(user_id, movie_id, list_type):
        list_id = Helpers.get_user_list_id_by_type_id(user_id, list_type)

        MovieList.objects.get(movie_id = movie_id, list_id = list_id).delete()

    def remove_rating(user_id, movie_id):
        Rating.objects.get(movie_id = movie_id, user_id = user_id).delete()

    def remove_watched(user_id, movie_id, list_type):
        DataBaseHandler.remove_movie_from_list(user_id=user_id, movie_id=movie_id, list_type=list_type)
        DataBaseHandler.remove_rating(user_id=user_id, movie_id=movie_id)

    #melhorar test, testar para ambos ifs
    def add_to_list(user_id, movie_id, list_type):
        list_id = Helpers.get_user_list_id_by_type_id(user_id, list_type)
        is_on_list = MovieList.objects.filter(movie_id = movie_id, list_id = list_id)

        #If in recommendation list, remove it
        if Helpers.is_movie_on_list(user_id, movie_id, 1):
            DataBaseHandler.remove_movie_from_list(user_id, movie_id, 1)

        if not is_on_list:
            movie_list_entry = MovieList(movie_id = movie_id, list_id = list_id)
            movie_list_entry.save()

    def add_to_list_external(user_id, tmdb_movie_id, tmdb_poster, tmdb_title, list_type):
        movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)
        if movie:
            movie_id = movie[0].movie_id
            DataBaseHandler.add_to_list (user_id, movie_id, list_type)
        else:
            DataBaseHandler.add_movie_to_database(tmdb_id=tmdb_movie_id)
            movie = Movie.objects.filter(tmdb_movie_id=tmdb_movie_id)
            if movie:
                movie_id = movie[0].movie_id
                DataBaseHandler.add_to_list(user_id, movie_id, list_type)
            else:
                print('Errro while adding new movie to list')
