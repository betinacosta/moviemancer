from django.test import TestCase
from moviemancer.models import *
from unittest import mock
from moviemancer.recommendation import Recommendation
from moviemancer.collaborative_filtering import CollaborativeFiltering

class RecommendationTestCase(TestCase):

    def setUp(self):
        Viwer.objects.create(user_id=77, name="hermoione", email="batata@batatinha.com")

        Type.objects.create(type_id=90, type_name="recommendation")
        Type.objects.create(type_id=91, type_name="watchlist")
        Type.objects.create(type_id=92, type_name="watchedlist")

        List.objects.create(list_id=33, user_id=77, type_id=90)
        List.objects.create(list_id=34, user_id=77, type_id=91)
        List.objects.create(list_id=35, user_id=77, type_id=92)

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

    def test_should_remove_repeated_movies_from_list(self):
        input_list = [67,3,4]
        new_list = Recommendation.remove_repeated_recommendations(user_id=77, reco_list=input_list, list_name=90)

        self.assertEqual(new_list, [3,4])

    @mock.patch('moviemancer.recommendation.Recommendation.remove_repeated_recommendations')
    def test_should_remove_repeated_movies_from_all_user_lists(self, mock_remove_repeated_recommendations):
        Recommendation.remove_repeated_movies_from_user_lists(user_id=77, input_list=[3,4])

        self.assertEqual(mock_remove_repeated_recommendations.call_count, 3)

    @mock.patch('moviemancer.collaborative_filtering.CollaborativeFiltering.generate_prediction')
    @mock.patch('moviemancer.recommendation.Recommendation.remove_repeated_movies_from_user_lists')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_recommendation_to_database')
    @mock.patch('moviemancer.recommendation.Recommendation.complete_recommendation')
    def test_should_create_user_recommendation(self, mock_generate_prediction, mock_remove_repeated_movies_from_user_lists, mock_add_recommendation_to_database, mock_complete_recommendation):
        Recommendation.create_user_recommendation(user_id=77)

        mock_generate_prediction.assert_called()
        mock_remove_repeated_movies_from_user_lists.assert_called()
        mock_add_recommendation_to_database.assert_called()
        mock_complete_recommendation.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.get_best_ratted_movies_by_user')
    @mock.patch('moviemancer.recommendation.Recommendation.get_similar_movies')
    @mock.patch('moviemancer.recommendation.Recommendation.remove_repeated_movies_from_user_lists')
    def test_should_complete_user_recommendation(self, mock_get_best_ratted_movies_by_user, mock_get_similar_movies, mock_remove_repeated_movies_from_user_lists):
        Recommendation.complete_recommendation(reco_list=[], user_id=77)

        mock_get_best_ratted_movies_by_user.assert_called()
        mock_remove_repeated_movies_from_user_lists.assert_called()

        self.assertEqual(mock_get_similar_movies.call_count, 2)