# -*- coding: utf-8 -*-
from moviemancer.tmdb_handler import TMDbHandler
from moviemancer.database_handlers import DataBaseHandler
from moviemancer.helpers import Helpers

class Recommendation:

    def is_inside_rage(min, max, value):
        if value >= min and value <= max:
            return True
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
        return False

    def filter_recommendation(genres, min_year, max_year, min_runtime, max_runtime, language, user_id):
        reco = Helpers.movie_by_user_list(user_id, 'recommendation')
        filtered_reco = []

        for r in reco:
            a = Recommendation.is_inside_rage(min_year, max_year, r.year)
            b = Recommendation.is_inside_rage(min_runtime, max_runtime, r.runtime)
            c = Recommendation.compare_genres(genres, r.genres)
            d = Recommendation.compare_languages(language, r.language)
            if a and b and c and d:
                filtered_reco.append({'movie_id': r.movie_id, 'tmdb_movie_id': r.tmdb_movie_id, 'tmdb_poster': r.tmdb_poster, 'tmdb_title': r.tmdb_title, 'tmdb_rating': r.tmdb_rating})

        return filtered_reco

    def get_similar_movies(movie_id):
        similar_movies = []

        tmdb_movie_id = Helpers.get_tmdb_id_by_movie_id(movie_id)
        tmdb_similar_movies = TMDbHandler.get_tmdb_similar_movies(tmdb_movie_id)

        for tmdb_id in tmdb_similar_movies:
            if not Helpers.is_movie_on_database(tmdb_id):
                DataBaseHandler.add_movie_to_database(tmdb_id)

            similar_movies.append(Helpers.get_movie_id_by_tmdb_id(tmdb_id))
        return similar_movies

    def remove_repeated_recommendations(user_id, reco_list, list_name):
        for item in Helpers.movie_id_by_user_list(user_id, list_name):
            if item.movie_id in reco_list:
                reco_list.remove(item.movie_id)
        return reco_list

    def remove_repeated_movies_from_user_lists(user_id, input_list):
        input_list = Recommendation.remove_repeated_recommendations(user_id, input_list, 1)
        input_list = Recommendation.remove_repeated_recommendations(user_id, input_list, 2)
        input_list = Recommendation.remove_repeated_recommendations(user_id, input_list, 3)

        return input_list
