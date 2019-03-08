from django.test import TestCase
from moviemancer.reco_refactor import *
from moviemancer.models import *
from unittest import mock
from moviemancer.recommendation import Recommendation

class RecommendationTestCase(TestCase):

    def setUp(self):
        Viwer.objects.create(user_id=77, name="hermoione", email="batata@batatinha.com")

        Type.objects.create(type_id=90, type_name="recommendation")

        List.objects.create(list_id=33, user_id=77, type_id=90)

        Movie.objects.create(movie_id=67, tmdb_movie_id=66, tmdb_title="Best Movie", tmdb_rating=7, year=1983, runtime=120, genres='35,18')

        MovieList.objects.create(movie_list_id=44, movie_id=67, list_id=33)

    def test_should_return_filtered_recommendation(self):
        filter = Recommendation.filter_recommendation(genres='35,18',min_year=1919,max_year=2017,min_runtime=50,max_runtime=300,language=0,user_id=77)
        expected = [{"movie_id": 67, "tmdb_movie_id": 66, "tmdb_poster": "", "tmdb_title": "Best Movie", "tmdb_rating": 7}]

        self.assertEqual(filter, expected)

    def test_should_return_empty_for_filtered_recommendation(self):
        filter = Recommendation.filter_recommendation(genres='18',min_year=2011,max_year=2012,min_runtime=50,max_runtime=300,language='pt',user_id=77)

        self.assertEqual(filter, [])

    def test_should_return_true_when_inside_range(self):
        self.assertTrue(Recommendation.is_inside_rage(1920, 2017, 1980))

    def test_should_return_false_when_outside_range(self):
        self.assertFalse(Recommendation.is_inside_rage(1920, 2003, 2017))

    def test_should_return_true_if_one_genre_match(self):
        self.assertTrue(Recommendation.compare_genres('35,18', '55,18,13'))

    def test_should_return_true_if_all_genres_match(self):
        self.assertTrue(Recommendation.compare_genres('35,18', '35,18'))

    def test_should_return_true_if_genres_is_zero(self):
        self.assertTrue(Recommendation.compare_genres(0, '35,18'))

    def test_should_return_false_if_genres_does_not_match(self):
        self.assertFalse(Recommendation.compare_genres('55,30,40', '35,18'))

    def test_should_return_true_if_languages_match(self):
        self.assertTrue(Recommendation.compare_languages('pt', 'pt'))

    def test_should_return_true_if_one_language_not_selected(self):
        self.assertTrue(Recommendation.compare_languages(0, 'pt'))

    def test_should_return_false_if_languages_does_not_match(self):
        self.assertFalse(Recommendation.compare_languages('en', 'pt'))

    @mock.patch('moviemancer.helpers.Helpers.get_tmdb_id_by_movie_id')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_similar_movies')
    def test_should_return_similar_movies_by_movie_id(self, mock_get_tmdb_id_by_movie_id, mock_get_tmdb_similar_movies):
        similar_movies = Recommendation.get_similar_movies(movie_id=67)

        mock_get_tmdb_id_by_movie_id.assert_called()
        mock_get_tmdb_similar_movies.assert_called()
