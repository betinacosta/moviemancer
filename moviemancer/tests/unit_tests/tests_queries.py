from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *
from moviemancer.tests.unit_tests.database_stub import DatabaseStub
from unittest import mock
from moviemancer.helpers import Helpers

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

    def test_should_return_user_id_by_email(self):
        self.assertEqual(get_user_id_by_email("batata@batatinha.com"), 1)

    def test_should_return_tmdb_id_by_movie_id(self):
        self.assertEqual(get_tmdb_id_by_movie_id(1), 533)

    def test_should_return_movie_id_by_tmdb_id(self):
        self.assertEqual(get_movie_id_by_tmdb_id(533), 1)

    def test_should_return_true_if_movie_on_user_list(self):
        self.assertTrue(is_movie_on_list(1, 1, 1))

    def test_should_return_false_if_movie_not_on_user_list(self):
        self.assertFalse(is_movie_on_list(2, 1, 2))

    #IMDb
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

    def test_should_return_true_for_registered_user(self):
        self.assertTrue(user_exists("batata@batatinha.com"))

    def test_should_return_false_for_registered_user(self):
        self.assertTrue(user_exists("nope@nope.com"))

    def test_should_return_filtered_recommendation(self):
        filter = filter_recommendation('35,18',1919,2017,50,300,0,2)
        expected = [{"movie_id": 6, "tmdb_movie_id": 66, "tmdb_poster": "", "tmdb_title": "Best Movie", "tmdb_rating": 7}]

        self.assertEqual(filter, expected)

    def test_should_return_empty_for_filtered_recommendation(self):
        filter = filter_recommendation('18',2011,2012,50,300,'pt',2)

        self.assertEqual(filter, [])

    def test_should_return_true_when_inside_range(self):
        self.assertTrue(is_inside_rage(1920, 2017, 1980))

    def test_should_return_false_when_outside_range(self):
        self.assertFalse(is_inside_rage(1920, 2003, 2017))

    def test_should_return_true_if_one_genre_match(self):
        self.assertTrue(compare_genres('35,18', '55,18,13'))

    def test_should_return_true_if_all_genres_match(self):
        self.assertTrue(compare_genres('35,18', '35,18'))

    def test_should_return_true_if_genres_is_zero(self):
        self.assertTrue(compare_genres(0, '35,18'))

    def test_should_return_false_if_genres_does_not_match(self):
        self.assertFalse(compare_genres('55,30,40', '35,18'))

    def test_should_return_true_if_languages_match(self):
        self.assertTrue(compare_languages('pt', 'pt'))

    def test_should_return_true_if_one_language_not_selected(self):
        self.assertTrue(compare_languages(0, 'pt'))

    def test_should_return_false_if_languages_does_not_match(self):
        self.assertFalse(compare_languages('en', 'pt'))

    def test_should_return_better_rated_movies_according_to_trashold(self):
        better_rated=[3, 4]
        self.assertEqual(get_better_ratted_movies_by_user(user_id=1, trashold=3), better_rated)

    def test_should_return_poster_image_link(self):
        poster_link='http://image.tmdb.org/t/p/original/123'
        self.assertEqual(get_poster_link(poster_path='/123'), poster_link)

    def test_should_return_formatted_year(self):
        year='1984'
        self.assertEqual(get_formatted_year('1984-03-02'), year)

    # def test_should_return_list_with_similar_movies(self):
    #     self.assertTrue(get_similar_movies(movie_id=96))

    # @mock.patch('moviemancer.queries.get_tmdb_similar_movies')
    # def test_should_generate_list_with_similar_movies(self, mock_get_tmdb_similar_movies):
    #     mock_get_tmdb_similar_movies.assert_called()
