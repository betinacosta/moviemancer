# -*- coding: utf-8 -*-
from moviemancer.models import *
from decimal import Decimal, ROUND_HALF_UP

class Helpers:

    def convert_tmdb_rating(tmdb_rating):
        return Decimal((tmdb_rating/2)).quantize(0, ROUND_HALF_UP)

    def formate_date_to_year(full_date):
        return full_date.split('-')[0]

    def get_comma_separeted_genres(genre_list):
        genres = []
        for genre in genre_list:
            genres.append(str(genre['id']))

        genres = ','.join(genres)
        return genres

    def get_user_list_id_by_type_id(user_id, type_id):
        user_list = List.objects.get(user_id = user_id, type_id = type_id)
        return user_list.list_id

    def get_user_list_id_by_type_name(user_id, list_type):
        type_id = Type.objects.get(type_name=list_type).type_id
        return Helpers.get_user_list_id_by_type_id(user_id=user_id, type_id=type_id)

    def is_movie_on_list (user_id, movie_id, type_id):
        list_id = Helpers.get_user_list_id_by_type_id(user_id, type_id)

        movie_list = MovieList.objects.filter(movie_id = movie_id, list_id = list_id)

        if not movie_list:
            return False
        return True

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

    def get_user_rate_to_movie(movie_id, user_id):
        rate_id = 0
        movie_rate = 0
        for item in Rating.objects.raw("SELECT * FROM rating WHERE rating.user_id = %s AND movie_id = %s", [user_id, movie_id]):
            rate_id = item.rate_id

        for item in Rate.objects.raw("SELECT * FROM rate WHERE rate_id = %s", [rate_id]):
            movie_rate = item.rate

        return movie_rate

    def get_rated_movies_by_user(user_id):
        movies =[]
        rate_list = {}

        for item in Helpers.movie_id_by_user_list(user_id, 3):
            movies.append(item.movie_id)

        for movie in movies:
            rate = Helpers.get_user_rate_to_movie(movie, user_id)
            rate_list.update({movie: rate})

        return rate_list

    def get_user_id_by_email(email):
        return Viwer.objects.get(email = email).user_id

    def get_tmdb_id_by_movie_id(movie_id):
        return Movie.objects.get(movie_id=movie_id).tmdb_movie_id

    def get_movie_id_by_tmdb_id(tmdb_movie_id):
        return Movie.objects.get(tmdb_movie_id=tmdb_movie_id).movie_id

    def get_movie_title_internal(movie_id):
        return Movie.objects.get(movie_id = movie_id).tmdb_title

    def get_movie_poster_internal(movie_id):
        return Movie.objects.get(movie_id = movie_id).tmdb_poster

    #refactor duplication with get_watched_list and get_recommendation_list
    def get_watchedlist (user):
        watched_list = []
        list_id = Helpers.get_user_list_id_by_type_id(user, 3)
        movies = MovieList.objects.filter(list_id = list_id)

        for m in movies:
            watched_list.append({
                'movie_id': m.movie_id,
                'tmdb_movie_id': Helpers.get_tmdb_id_by_movie_id(m.movie_id),
                'title': Helpers.get_movie_title_internal(m.movie_id),
                'poster': Helpers.get_movie_poster_internal(m.movie_id),
                'rating': Helpers.get_user_rate_to_movie(m.movie_id, user)
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
                'tmdb_movie_id': Helpers.get_tmdb_id_by_movie_id(m.movie_id),
                'title': Helpers.get_movie_title_internal(m.movie_id),
                'poster': Helpers.get_movie_poster_internal(m.movie_id),
                'tmdb_rating': Helpers.get_tmdb_rating_internal(m.movie_id)
            })

        return watchlist

    def get_recommendation_list(user_id, type_id):
        movies = Helpers.movie_by_user_list(user_id, 'recommendation')
        recommendation_list = []

        for m in movies:
            recommendation_list.append({'movie_id': m.movie_id, 'tmdb_movie_id': m.tmdb_movie_id, 'tmdb_poster': m.tmdb_poster, 'tmdb_title': m.tmdb_title, 'tmdb_rating': m.tmdb_rating})

        return recommendation_list

    def user_exists(user_email):
        if Viwer.objects.filter(email = user_email).exists():
            return True
        return False

    def get_user_id(email):
        return Viwer.objects.get(email = email).user_id

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

    def get_user(email):
        user = Viwer.objects.get(email = email)
        return {'user_id': user.user_id, 'name': user.name, 'email': user.email,}

    def get_comments(movie_tmdb_id):
        movie_id = Helpers.get_movie_id_by_tmdb_id(movie_tmdb_id)
        comments = Comments.objects.filter(movie_id = movie_id)
        commnets_by_movie = []

        for comment in comments:
            user = Viwer.objects.filter(user_id = comment.user_id)
            name = user[0].name
            rate = Helpers.get_user_rate_to_movie(movie_id, comment.user_id)
            commnets_by_movie.append({"comment_id": comment.comment_id, "user_name": name,"comment": comment.comment, "rate": rate})
        return commnets_by_movie

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

    def get_best_ratted_movies_by_user(user_id, trashold):
        best_ratted = []
        movie_ids = []
        for item in Helpers.movie_id_by_user_list(user_id, 3):
            movie_ids.append(item.movie_id)

        for movie_id in movie_ids:
            rate = Helpers.get_user_rate_to_movie(movie_id=movie_id, user_id=user_id)
            if rate >= trashold:
                best_ratted.append(movie_id)

        return best_ratted

    def is_movie_on_database(tmdb_movie_id):
        movie = Movie.objects.filter(tmdb_movie_id = tmdb_movie_id)

        if not movie:
            return False
        return True

