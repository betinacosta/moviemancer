# -*- coding: utf-8 -*-
from moviemancer.models import *
import json
import hashlib
import tmdbsimple as tmdb
import time
from decimal import Decimal, ROUND_HALF_UP
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
        if not movie:
            DataBaseHandler.add_movie_to_database(tmdb_id=tmdb_movie_id)
            movie = Movie.objects.filter(tmdb_movie_id=tmdb_movie_id)

        DataBaseHandler.add_to_list(user_id=user_id, movie_id=movie[0].movie_id, list_type=list_type)

    def rate_movie(user_id, movie_id, local_rate_id):
        DataBaseHandler.add_rating_to_movie(user_id, movie_id, local_rate_id)

        if Helpers.is_movie_on_list(user_id, movie_id, 2):
            DataBaseHandler.remove_movie_from_list(user_id, movie_id, 2)

        DataBaseHandler.add_to_list(user_id, movie_id, 3)

    def rate_external_movie(user_id, user_rating, tmdb_movie_id, tmdb_poster, tmdb_title):
        movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

        if movie:
            movie_id = movie[0].movie_id
            DataBaseHandler.rate_movie(user_id, movie_id, user_rating)
            return True
        else:
            DataBaseHandler.add_movie_to_database(tmdb_id=tmdb_movie_id)
            movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)
            if movie:
                movie_id = movie[0].movie_id
                DataBaseHandler.rate_movie (user_id, movie_id, user_rating)
                return True
            return False

    def create_user(name, email, password):
        user = Viwer.objects.filter(email = email)

        if not user:
            hash_password = hashlib.sha224(password.encode('utf-8')).hexdigest()

            user = Viwer(name=name, email=email, password=hash_password)
            user.save()

        return None

    def create_list_to_user(user_id, type_id):
        user_list = List.objects.filter(user_id = user_id, type_id = type_id)

        if not user_list:
            user_list = List(user_id = user_id, type_id = type_id)
            user_list.save()

    def register_user(name, email, password):
        DataBaseHandler.create_user(name, email, password)

        user_id = Helpers.get_user_id(email=email)

        DataBaseHandler.create_list_to_user(user_id, 1)
        DataBaseHandler.create_list_to_user(user_id, 2)
        DataBaseHandler.create_list_to_user(user_id, 3)

        return user_id

    def update_user_info(user_id, email, name, password):
        user = Helpers.handle_user_update_info(user_id, email, name, password)
        user.save()

    def authenticate_user(email, password):
        hash_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        user = Viwer.objects.filter(email=email, password=hash_password)

        if user:
            return True
        return False

    def add_comment(movie_tmdb_id, user_id, comment):
        movie_id = Helpers.get_movie_id_by_tmdb_id(movie_tmdb_id)

        comment = Comments(movie_id = movie_id, user_id = user_id, comment = comment)
        comment.save()

    def delete_comment(comment_id):
        Comments.objects.get(comment_id = comment_id).delete()

        if not Comments.objects.filter(comment_id = comment_id):
            return True
        return False

    def add_recommendation_to_database(reco_list, user_id):
        list_id = Helpers.get_user_list_id_by_type_id(user_id, 1)
        reco_list = list(set(reco_list))

        for movie_id in reco_list:
            reco = MovieList(movie_id=movie_id, list_id=list_id)
            reco.save()