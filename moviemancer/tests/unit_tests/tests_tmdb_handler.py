from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *
from moviemancer.tmdb_handler import TMDbHandler
from moviemancer.tests.unit_tests.database_stub import DatabaseStub
from unittest import mock

class TMDbHandlerTestCase(TestCase):
    def setUp(self):
        DatabaseStub.create_database_stub()

    def test_should_return_movie_title_from_tmdb(self):
        self.assertEqual(TMDbHandler.get_movie_title(55), "Amores Brutos")

    def test_should_convert_tmdb_rating_to_four(self):
        self.assertEqual(TMDbHandler.get_tmdb_movie_rating(55),4)

    def test_should_generate_similar_movies_by_tmdb_id_list(self):
        self.assertTrue(TMDbHandler.get_tmdb_similar_movies(5))

    def test_should_return_link_to_movie_poster(self):
        self.assertIn('http://image.tmdb.org/t/p/original', TMDbHandler.get_movie_poster(55))

    def test_should_return_tmdb_movie_language(self):
        self.assertEqual(TMDbHandler.get_tmdb_movie_language(55), "es")

    def test_should_return_tmdb_movie_runtime_if_available_in_tmdb(self):
        self.assertEqual(TMDbHandler.get_tmdb_movie_runtime(55), 154)

    def test_should_return_tmdb_movie_year(self):
        self.assertEqual(TMDbHandler.get_tmdb_movie_year(55), '2000')

    def test_should_return_tmdb_movie_genres_id_separated_by_coma(self):
        self.assertEquals(TMDbHandler.get_tmdb_movie_genres_id(55), '18,53')