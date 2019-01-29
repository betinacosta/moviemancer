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