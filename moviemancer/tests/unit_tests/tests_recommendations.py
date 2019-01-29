from django.test import TestCase
from moviemancer.reco_refactor import *
from moviemancer.models import *
from unittest import mock

class RecommendationTestCase(TestCase):

    def setUp(self):
        Viwer.objects.create(user_id=1, name="hermoione", email="batata@batatinha.com")

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=2, type_name="watchlist")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=1, user_id=1, type_id=1)
        List.objects.create(list_id=2, user_id=1, type_id=2)
        List.objects.create(list_id=3, user_id=1, type_id=3)

        Movie.objects.create(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=8, year=1998, runtime=93)
        Movie.objects.create(movie_id=2, tmdb_movie_id=123, tmdb_title="Monty Python", tmdb_rating=9, year=1974, runtime=120)

        Rate.objects.create(rate_id=1, rate=1)
        Rate.objects.create(rate_id=2, rate=2)
        Rate.objects.create(rate_id=3, rate=3)
        Rate.objects.create(rate_id=4, rate=4)
        Rate.objects.create(rate_id=5, rate=5)

        Rating.objects.create(rating_id=1, user_id=1, movie_id=1, rate_id=2)
        Rating.objects.create(rating_id=2, user_id=1, movie_id=2, rate_id=4)

        MovieList.objects.create(movie_list_id=1, movie_id=1, list_id=3)
        MovieList.objects.create(movie_list_id=2, movie_id=2, list_id=3)

    # def test_should_return_user_movies_dataset(self):
    #     self.assertEqual(get_dataset(), {1: {1: 2, 2: 4}})