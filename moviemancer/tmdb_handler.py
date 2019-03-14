# -*- coding: utf-8 -*-

import tmdbsimple as tmdb
from moviemancer.helpers import Helpers

tmdb.API_KEY = '5880f597a9fab4f284178ffe0e1f0dba'

class TMDbHandler():

    def get_movie_title(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info(language = 'pt-BR')

        return tmdb_movie.title

    def get_tmdb_movie_rating(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info()

        return Helpers.convert_tmdb_rating(tmdb_movie.vote_average)

    def get_tmdb_similar_movies(tmdb_movie_id):
        similar_movies = []
        movie = tmdb.Movies(tmdb_movie_id)
        response = movie.similar_movies(language = 'pt-BR', page=1)

        for item in response['results']:
            similar_movies.append(item['id'])
        return similar_movies

    def get_movie_poster(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info(language = 'pt-BR')

        return 'http://image.tmdb.org/t/p/original' + tmdb_movie.poster_path

    def get_tmdb_movie_language(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info()

        return tmdb_movie.original_language

    def get_tmdb_movie_runtime(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info()

        if tmdb_movie.runtime == 0 or tmdb_movie.runtime == 'None':
            return 50

        return tmdb_movie.runtime

    def get_tmdb_movie_year(tmdb_id):
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info()

        return Helpers.formate_date_to_year(tmdb_movie.release_date)

    def get_tmdb_movie_genres_id(tmdb_id):
        genres = []
        tmdb_movie = tmdb.Movies(tmdb_id)
        tmdb_movie.info(language = 'pt-BR')

        return Helpers.get_comma_separeted_genres(tmdb_movie.genres)