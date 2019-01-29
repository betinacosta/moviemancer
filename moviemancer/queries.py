# -*- coding: utf-8 -*-
from moviemancer.models import *
import json
import hashlib
import tmdbsimple as tmdb
import time
from decimal import Decimal, ROUND_HALF_UP
from moviemancer.tmdb_handler import TMDbHandler
from moviemancer.database_handlers import DataBaseHandler
from moviemancer.helpers import Helpers

tmdb.API_KEY = '5880f597a9fab4f284178ffe0e1f0dba'

def get_all_user_lists_ids(user_id):
    lists = []
    for item in List.objects.raw("SELECT list_ID FROM list WHERE user_id = %s", [user_id]):
        lists.append(item.list_id)
    return lists

#remove this or movie_id_by_user_list
def movie_by_user_list(user_id, list_name):
    for item in Type.objects.raw("SELECT * FROM type WHERE type_name = %s", [list_name]):
        type_id = item.type_id

    for item in List.objects.filter(user_id = user_id, type_id = type_id):
        list_id = item.list_id

    movie_list = Movie.objects.raw("SELECT * from movie INNER JOIN movie_list ON list_id = %s AND movie_list.movie_id = movie.movie_id", [list_id])
    return movie_list

#remove this or movie_by_user_list
def movie_id_by_user_list(user_id, type_id):
    list_id = Helpers.get_user_list_id_by_type_id(user_id, type_id)
    movie_list = MovieList.objects.filter(list_id = list_id)

    return movie_list

def get_rated_movies_by_user(user_id):
    movies =[]
    rate_list = {}

    for item in movie_id_by_user_list(user_id, 3):
        movies.append(item.movie_id)

    for movie in movies:
        rate = get_user_rate_to_movie(movie, user_id)
        rate_list.update({movie: rate})

    return rate_list

def get_user_rate_to_movie(movie_id, user_id):
    rate_id = 0
    movie_rate = 0
    for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
        rate_id = item.rate_id

    for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id]):
        movie_rate = item.rate

    return movie_rate

def get_user_id_by_email(email):
    user = Viwer.objects.filter(email = email)

    return user[0].user_id

#in other class
def get_tmdb_id_by_movie_id(movie_id):
   return Movie.objects.get(movie_id=movie_id).tmdb_movie_id

def get_movie_id_by_tmdb_id(tmdb_movie_id):
    return Movie.objects.get(tmdb_movie_id=tmdb_movie_id).movie_id

def is_movie_on_list (user_id, movie_id, type_id):
    list_id = Helpers.get_user_list_id_by_type_id(user_id, type_id)

    movie_list = MovieList.objects.filter(movie_id = movie_id, list_id = list_id)

    if not movie_list:
        return False
    return True

def get_movie_title_internal(movie_id):
    movie = Movie.objects.filter(movie_id = movie_id)

    return movie[0].tmdb_title

def get_movie_poster_internal(movie_id):
    movie = Movie.objects.filter(movie_id = movie_id)

    return movie[0].tmdb_poster

def get_movie_tmdb_id(movie_id):
    return Movie.objects.get(movie_id = movie_id).tmdb_movie_id

#refactor duplication with get_watched_list and get_recommendation_list
def get_watchedlist (user):
    watched_list = []
    list_id = Helpers.get_user_list_id_by_type_id(user, 3)
    movies = MovieList.objects.filter(list_id = list_id)

    for m in movies:
        watched_list.append({
            'movie_id': m.movie_id,
            'tmdb_movie_id': get_movie_tmdb_id(m.movie_id),
            'title': get_movie_title_internal(m.movie_id),
            'poster': get_movie_poster_internal(m.movie_id),
            'rating': get_user_rate_to_movie(m.movie_id, user)
        })

    return watched_list

def get_tmdb_rating_internal(movie_id):
    return Movie.objects.get(movie_id = movie_id).tmdb_rating

def get_watchlist(user):
    watchlist = []
    list_id = Helpers.get_user_list_id_by_type_id(user, 2)
    movies = MovieList.objects.filter(list_id = list_id)

    for m in movies:
        watchlist.append({
            'movie_id': m.movie_id,
            'tmdb_movie_id': get_movie_tmdb_id(m.movie_id),
            'title': get_movie_title_internal(m.movie_id),
            'poster': get_movie_poster_internal(m.movie_id),
            'tmdb_rating': get_tmdb_rating_internal(m.movie_id)

        })

    return watchlist

def get_recommendation_list(user_id, type_id):
    movies = movie_by_user_list(user_id, 'recommendation')
    recommendation_list = []

    for m in movies:
        recommendation_list.append({'movie_id': m.movie_id, 'tmdb_movie_id': m.tmdb_movie_id, 'tmdb_poster': m.tmdb_poster, 'tmdb_title': m.tmdb_title, 'tmdb_rating': m.tmdb_rating})

    return recommendation_list

def user_exists(user_email):
    if Viwer.objects.filter(email = user_email).exists():
        return True
    return True

def filter_recommendation(genres, minYear, maxYear, minRuntime, maxRuntime, language, user_id):
    reco = movie_by_user_list(user_id, 'recommendation')
    filtered_reco = []

    for r in reco:
        a = is_inside_rage(minYear, maxYear, r.year)
        b = is_inside_rage(minRuntime, maxRuntime, r.runtime)
        c = compare_genres(genres, r.genres)
        d = compare_languages(language, r.language)
        if a and b and c and d:
            filtered_reco.append({'movie_id': r.movie_id, 'tmdb_movie_id': r.tmdb_movie_id, 'tmdb_poster': r.tmdb_poster, 'tmdb_title': r.tmdb_title, 'tmdb_rating': r.tmdb_rating})

    return filtered_reco

def is_inside_rage(min, max, value):
    if value >= min and value <= max:
        return True
    else:
        return False

def compare_genres(g1, g2):

    if g1 == 0 or g2 == 0:
        return True

    g1 = g1.split(',')
    g2 = g2.split(',')

    if len(g1) > len(g2):
        bigger = g1
        smaller = g2
    else:
        bigger = g2
        smaller = g1

    for g in smaller:
        if g in bigger:
            return True

    return False

def compare_languages(l1, l2):
    if l1 == 0 or l2 == 0 or l1 == l2:
        return True
    else:
        return False

#UPDATE, DELETE, INSERT
def remove_watched(user_id, movie_id, list_type):
    DataBaseHandler.remove_movie_from_list(user_id, movie_id, list_type)
    DataBaseHandler.remove_rating(user_id, movie_id)

def add_to_list_external(user_id, tmdb_movie_id, tmdb_poster, tmdb_title, list_type):
    movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)
    if movie:
        movie_id = movie[0].movie_id
        add_to_list (user_id, movie_id, list_type)
    else:
        DataBaseHandler.add_movie_to_database(tmdb_id=tmdb_movie_id)
        movie = Movie.objects.filter(tmdb_movie_id=tmdb_movie_id)
        if movie:
            movie_id = movie[0].movie_id
            add_to_list (user_id, movie_id, list_type)
        else:
            print('Errro while adding new movie to list')

#melhorar test, testar para ambos ifs
def add_to_list (user_id, movie_id, list_type):
    list_id = Helpers.get_user_list_id_by_type_id(user_id, list_type)
    is_on_list = MovieList.objects.filter(movie_id = movie_id, list_id = list_id)

    #If in recommendation list, remove it
    if is_movie_on_list (user_id, movie_id, 1):
        DataBaseHandler.remove_movie_from_list(user_id, movie_id, 1)

    if not is_on_list:
        movie_list_entry = MovieList(movie_id = movie_id, list_id = list_id)
        movie_list_entry.save()

def rate_movie (user_id, movie_id, local_rate_id):

    #add rating
    DataBaseHandler.add_rating_to_movie(user_id, movie_id, local_rate_id)

    #check if it is on watchlist and remove it
    if is_movie_on_list(user_id, movie_id, 2):
        DataBaseHandler.remove_movie_from_list(user_id, movie_id, 2)

    #add to watched list
    add_to_list (user_id, movie_id, 3)

def rate_external_movie (user_id, user_rating, tmdb_movie_id, tmdb_poster, tmdb_title):
    movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

    if movie:
        movie_id = movie[0].movie_id
        rate_movie(user_id, movie_id, user_rating)
        return True
    else:
        DataBaseHandler.add_movie_to_database(tmdb_id=tmdb_movie_id)
        movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)
        if movie:
            movie_id = movie[0].movie_id
            rate_movie (user_id, movie_id, user_rating)
            return True
        else:
            return False

def register_user(name, email, password):
    create_user(name, email, password)

    user_id = get_user_id(email=email)

    create_list_to_user(user_id, 1)
    create_list_to_user(user_id, 2)
    create_list_to_user(user_id, 3)

    return user_id

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

def handle_user_update_info(user_id, email, name, password):
    old_user = Viwer.objects.filter(user_id=user_id)

    if not email or email == ' ':
        email = old_user[0].email
    if not name or name == ' ':
        name = old_user[0].name
    if not password or password == ' ':
        password = old_user[0].password
    else:
        password = hashlib.sha224(password.encode('utf-8')).hexdigest()

    return Viwer(user_id = user_id, name = name, email = email, password = password)

def update_user_info(user_id, email, name, password):
    user = handle_user_update_info(user_id, email, name, password)
    user.save()

#AUTHENTICATION HANDLERS

def authenticate_user(email, password):
    hash_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
    user = Viwer.objects.filter(email=email, password=hash_password)

    if user:
        return True
    return False

def get_user(email):
    user = Viwer.objects.get(email = email)

    user_info = {'user_id': user.user_id, 'name': user.name, 'email': user.email,}

    return user_info

def get_user_id(email):
    user = Viwer.objects.get(email = email)

    return user.user_id

#COMMENTS HANDLERS

def get_comments(movie_tmdb_id):
    movie_id = get_movie_id_by_tmdb_id(movie_tmdb_id)
    comments = Comments.objects.filter(movie_id = movie_id)
    commnets_by_movie = []

    for comment in comments:
        user = Viwer.objects.filter(user_id = comment.user_id)
        name = user[0].name
        rate = get_user_rate_to_movie(movie_id, comment.user_id)
        commnets_by_movie.append({"comment_id": comment.comment_id, "user_name": name,"comment": comment.comment, "rate": rate})
    return commnets_by_movie

def add_comment(movie_tmdb_id, user_id, comment):
    movie_id = get_movie_id_by_tmdb_id(movie_tmdb_id)

    comment = Comments(movie_id = movie_id, user_id = user_id, comment = comment)
    comment.save()

def delete_comment(comment_id):
    Comments.objects.get(comment_id = comment_id).delete()

    if not Comments.objects.filter(comment_id = comment_id):
        return True
    else:
        return False

def get_rated_movies():
    ratings = []
    rated_movies = []

    for m in Rating.objects.all():
        ratings.append(m.movie_id)
    ratings = list(set(ratings))

    for movie_id in ratings:
        movie_info = Movie.objects.get(movie_id = movie_id)
        rated_movies.append({'movie_id': movie_id, 'title': movie_info.tmdb_title, 'poster': movie_info.tmdb_poster})
    return rated_movies

def get_better_ratted_movies_by_user(user_id, trashold):
    better_ratted = []
    movie_ids = []
    for item in movie_id_by_user_list(user_id, 3):
        movie_ids.append(item.movie_id)

    for movie_id in movie_ids:
        rate = get_user_rate_to_movie(movie_id=movie_id, user_id=user_id)
        if rate >= trashold:
            better_ratted.append(movie_id)

    return better_ratted

def get_poster_link(poster_path):
    return 'http://image.tmdb.org/t/p/original' + poster_path

def get_formatted_year(year):
    return year.split('-')[0]

def is_movie_on_database(tmdb_movie_id):
    movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

    if not movie:
        return False
    return True

def get_similar_movies(movie_id):
    similar_movies = []

    tmdb_movie_id = get_tmdb_id_by_movie_id(movie_id)
    tmdb_similar_movies = TMDbHandler.get_tmdb_similar_movies(tmdb_movie_id)

    for tmdb_id in tmdb_similar_movies:
        if not is_movie_on_database(tmdb_id):
            DataBaseHandler.add_movie_to_database(tmdb_id)

        similar_movies.append(get_movie_id_by_tmdb_id(tmdb_id))
    return similar_movies