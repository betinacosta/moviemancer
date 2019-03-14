from django.test import TestCase
from moviemancer.collaborative_filtering import CollaborativeFiltering
from moviemancer.tests.unit_tests.database_stub import DatabaseStub
from moviemancer.models import *

class CollaborativeFilteringTestCase(TestCase):
    def setUp(self):
        Viwer.objects.create(user_id=1, name="hermoione", email="batata@batatinha.com")
        Viwer.objects.create(user_id=2, name="luna")

        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=3, user_id=1, type_id=3)

        List.objects.create(list_id=6, user_id=2, type_id=3)

        Movie.objects.create(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)
        Movie.objects.create(movie_id=2, tmdb_movie_id=123, tmdb_title="Monty Python", tmdb_rating=9, year=1974, runtime=120)
        Movie.objects.create(movie_id=3, tmdb_movie_id=344, tmdb_title="Blade Runner", tmdb_rating=7, year=1983, runtime=120)
        Movie.objects.create(movie_id=4, tmdb_movie_id=77, tmdb_title="Mean Girls", tmdb_rating=5, year=2004, runtime=120)

        Rate.objects.create(rate_id=1, rate=1)
        Rate.objects.create(rate_id=3, rate=3)
        Rate.objects.create(rate_id=4, rate=4)

        Rating.objects.create(rating_id=1, user_id=1, movie_id=3, rate_id=4)
        Rating.objects.create(rating_id=2, user_id=1, movie_id=2, rate_id=3)
        Rating.objects.create(rating_id=3, user_id=2, movie_id=1, rate_id=1)
        Rating.objects.create(rating_id=4, user_id=2, movie_id=4, rate_id=4)

        MovieList.objects.create(movie_list_id=1, movie_id=3, list_id=3)
        MovieList.objects.create(movie_list_id=2, movie_id=2, list_id=3)

        MovieList.objects.create(movie_list_id=3, movie_id=1, list_id=6)
        MovieList.objects.create(movie_list_id=4, movie_id=4, list_id=6)

    def test_should_return_formated_dataset(self):
        self.assertEqual(CollaborativeFiltering.get_dataset(), {1: {3: 4, 2: 3}, 2: {1: 1, 4: 4}})