from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *
from moviemancer.tests.unit_tests.database_stub import DatabaseStub

class QueriesTestCase(TestCase):
    def setUp(self):
        DatabaseStub.create_database_stub()

    def test_should_return_list_ids_by_user(self):
        list_ids_by_user = set(get_all_user_lists_ids(1))

        self.assertEqual(len(list_ids_by_user),3)

    def test_should_return_movie_raw_in_a_list_by_user(self):
        movie = Movie(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

        self.assertEqual(movie_by_user_list(1, "recommendation")[0], movie)

    def test_should_return_movie_object_in_a_list_by_user(self):
        movie_list = MovieList(movie_list_id=1, movie_id=1, list_id=1)

        self.assertEqual(list(movie_id_by_user_list(1,1)), [movie_list])

    def test_should_return_rated_movies_by_user(self):
        self.assertEqual(get_rated_movies_by_user(1), {3: 4, 4: 3})

    def test_should_return_user_rate_to_movie(self):
        self.assertEqual(get_user_rate_to_movie(3, 1), 4)

    def test_should_return_list_by_user(self):
        self.assertEqual(get_user_list_id_by_type_id(1, 3), 3)

    def test_should_return_user_id_by_email(self):
        self.assertEqual(get_user_id_by_email("batata@batatinha.com"), 1)

    def test_should_return_list_with_tmdb_movie_ids(self):
        self.assertEqual(get_tmdb_movies_id(), [533, 123, 344, 77, 55])

    def test_should_return_tmdb_id_by_movie_id(self):
        self.assertEqual(get_tmdb_id_by_movie_id(1), 533)

    def test_should_return_movie_id_by_tmdb_id(self):
        self.assertEqual(get_movie_id_by_tmdb_id(533), 1)

    def test_should_return_true_if_movie_on_user_list(self):
        self.assertTrue(is_movie_on_list(1, 1, 1))

    def test_should_return_false_if_movie_not_on_user_list(self):
        self.assertFalse(is_movie_on_list(2, 1, 2))

    #IMDb
    def test_should_return_movie_title_from_tmdb(self):
        self.assertEqual(get_movie_title(55), "Amores Brutos")

    def test_should_return_link_to_movie_poster(self):
        self.assertIn('http://image.tmdb.org/t/p/original', get_movie_poster(55))

    def test_should_return_link_to_movie_poster_by_movie_id(self):
        self.assertIn('http://image.tmdb.org/t/p/original', get_movie_poster_internal(5))

    def test_should_return_watchedlist_for_a_user(self):
        movie_list = [
            {'movie_id': 3, 'poster': '', 'rating': 4, 'title': 'Blade Runner', 'tmdb_movie_id': 344},
            {'movie_id': 4, 'poster': '', 'rating': 3, 'title': 'Mean Girls', 'tmdb_movie_id': 77}
        ]
        self.assertEqual(get_watchedlist(1), movie_list)

    def test_should_return_tmdb_rating_by_movie_id(self):
        self.assertEqual(get_tmdb_rating_internal(1), 6)

    def test_should_return_watchlist_for_a_user(self):
        movie_list = [
            {'movie_id': 1, 'poster': '', 'title': 'Princess Bride', 'tmdb_movie_id': 533, 'tmdb_rating': 6}
        ]
        self.assertEqual(get_watchlist(1), movie_list)

    def test_should_return_recommendation_list_for_a_user(self):
        movie_list = [
            {'movie_id': 1, 'tmdb_movie_id': 533, 'tmdb_poster': '', 'tmdb_rating': 6, 'tmdb_title': 'Princess Bride'}
        ]
        self.assertEqual(get_recommendation_list(1, 3), movie_list)