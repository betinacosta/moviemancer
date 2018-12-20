from django.test import TestCase
from moviemancer.queries import get_list_id_by_user, movie_by_user_list, movie_id_by_user_list
from moviemancer.models import *
from moviemancer.tests.unit_tests.database_stub import DatabaseStub

class QueriesTestCase(TestCase):
    def setUp(self):
        DatabaseStub.create_database_stub()

    def test_should_return_list_ids_by_user(self):
        list_ids_by_user = set(get_list_id_by_user(1))

        self.assertEquals(len(list_ids_by_user),3)

    def test_should_return_movie_raw_in_a_list_by_user(self):
        movie = Movie(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

        self.assertEquals(movie_by_user_list(1, "recommendation")[0], movie)

    def test_should_return_movie_object_in_a_list_by_user(self):
        movie_list = MovieList(movie_list_id=1, movie_id=1, list_id=1)

        self.assertEqual(list(movie_id_by_user_list(1,1)), [movie_list])
