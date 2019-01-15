from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *

class DatabaseTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(tmdb_movie_id=3, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

    def test_should_add_new_movie_to_database(self):
        self.assertEqual(add_movie_to_database(543), 'Success')

    def test_should_return_error_if_movie_exists_in_db(self):
        self.assertEqual(add_movie_to_database(3), 'Error: movie already exists')

    def test_should_add_new_rate_to_movie(self):
        add_rating_to_movie(user_id=5, movie_id=44, local_rate_id=3)
        self.assertTrue(Rating.objects.get(user_id=5, movie_id=44))

    def test_should_update_existing_movie_rate(self):
        add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=3)
        add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=5)

        self.assertTrue(Rating.objects.get(user_id=5, movie_id=55, rate_id=5))