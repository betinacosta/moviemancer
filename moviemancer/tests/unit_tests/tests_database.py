from django.test import TestCase
from moviemancer.models import *
from unittest import mock
from moviemancer.database_handlers import DataBaseHandler
from moviemancer.helpers import Helpers

class DatabaseTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(movie_id=35, tmdb_movie_id=3, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)
        Movie.objects.create(movie_id=36, tmdb_movie_id=9, tmdb_title="Princess", tmdb_rating=4, year=1944, runtime=93)

        Viwer.objects.create(name="luna")
        Viwer.objects.create(user_id=88, name='test', email='bla@test', password='secure')

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=2, type_name="watchlist")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=11, user_id=1, type_id=1)
        List.objects.create(list_id=22, user_id=1, type_id=2)
        List.objects.create(list_id=33, user_id=1, type_id=3)

        MovieList.objects.create(movie_list_id=13, movie_id=35, list_id=11)
        MovieList.objects.create(movie_list_id=14, movie_id=36, list_id=22)

        Comments.objects.create(comment_id=99, user_id=77, movie_id=99, comment='muito bom, 2 estrelas')

    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_movie_poster')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_movie_title')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_movie_rating')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_movie_language')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_movie_runtime')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_movie_genres_id')
    @mock.patch('moviemancer.tmdb_handler.TMDbHandler.get_tmdb_movie_year')
    @mock.patch('moviemancer.models.Movie.save')
    def test_should_add_new_movie_to_database(self, mock_poster, mock_save, mock_title, mock_rating, mock_language, mock_runtime, mock_genres, mock_year):
        DataBaseHandler.add_movie_to_database(543)
        mock_poster.assert_called()
        mock_title.assert_called()
        mock_rating.assert_called()
        mock_language.assert_called()
        mock_runtime.assert_called()
        mock_genres.assert_called()
        mock_year.assert_called()
        mock_save.assert_called()

    def test_should_return_error_if_movie_exists_in_db(self):
        self.assertEqual(DataBaseHandler.add_movie_to_database(3), 'Error: movie already exists')

    def test_should_add_new_rate_to_movie(self):
        DataBaseHandler.add_rating_to_movie(user_id=5, movie_id=44, local_rate_id=3)
        self.assertTrue(Rating.objects.filter(user_id=5, movie_id=44))

    def test_should_update_existing_movie_rate(self):
        DataBaseHandler.add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=3)
        DataBaseHandler.add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=5)

        self.assertTrue(Rating.objects.filter(user_id=5, movie_id=55, rate_id=5))

    @mock.patch('moviemancer.models.MovieList.delete')
    def test_should_remove_movie_from_list(self, mock_delete):
        MovieList.objects.create(movie_id=35, list_id=33)
        DataBaseHandler.remove_movie_from_list(user_id=1, movie_id=35, list_type=3)

        mock_delete.assert_called()

    @mock.patch('moviemancer.models.Rating.delete')
    def test_should_remove_user_rating_to_given_movie(self, mock_delete):
        Rating.objects.create(user_id=1, movie_id=35, rate_id=4)
        DataBaseHandler.remove_rating(user_id=1, movie_id=35)

        mock_delete.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_movie_from_list')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_rating')
    def test_should_remove_movie_from_watched_list(self, mock_remove_rating, mock_remove_from_list):
        DataBaseHandler.remove_watched(user_id=1, movie_id=36, list_type=3)

        mock_remove_from_list.assert_called_with(user_id=1, movie_id=36, list_type=3)
        mock_remove_rating.assert_called_with(user_id=1, movie_id=36)

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_to_list')
    def test_should_create_movie_and_add_to_list(self, mock_add_to_list):
        DataBaseHandler.add_to_list_external(user_id=1, tmdb_movie_id=76203, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)
        movie = Movie.objects.get(tmdb_movie_id=76203)

        mock_add_to_list.assert_called_with(user_id=1, movie_id=movie.movie_id, list_type=3)

    def test_should_add_existent_movie_to_list(self):
        Movie.objects.create(movie_id=99, tmdb_movie_id=533, tmdb_title="Batatas Furiosas", tmdb_rating=6, year=1998, runtime=93)
        DataBaseHandler.add_to_list_external(user_id=1, tmdb_movie_id=533, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)

        self.assertTrue(MovieList.objects.filter(movie_id=99, list_id=33))
        self.assertTrue(len(Movie.objects.filter(tmdb_movie_id=533)) == 1)

    @mock.patch('moviemancer.models.MovieList.save')
    def test_should_add_movie_to_list(self, mock_save):
        DataBaseHandler.add_to_list(user_id=1, movie_id=66, list_type=1)

        mock_save.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_movie_from_list')
    def test_should_remove_from_recomendation_if_added_to_other_list(self, mock_remove_from_list):
        DataBaseHandler.add_to_list(user_id=1, movie_id=35, list_type=2)

        mock_remove_from_list.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_rating_to_movie')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_to_list')
    def test_should_add_movie_to_watchedlist_when_rated(self, mock_add_rating, mock_add_to_list):
        DataBaseHandler.rate_movie(user_id=1, movie_id=33, local_rate_id=5)

        mock_add_rating.assert_called()
        mock_add_to_list.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_rating_to_movie')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_movie_from_list')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_to_list')
    def test_should_remove_movie_from_watchlist_when_rated(self, mock_add_rating, mock_remove_from_list, mock_add_to_list):
        DataBaseHandler.rate_movie(user_id=1, movie_id=36, local_rate_id=5)

        mock_add_rating.assert_called()
        mock_remove_from_list.assert_called()
        mock_add_rating.assert_called()

    def test_should_add_new_movie_to_watchedlist_when_rated(self):
        DataBaseHandler.rate_external_movie(user_id=1, user_rating=3, tmdb_movie_id=99, tmdb_poster='bla.jpg', tmdb_title="The Amazing Papas")
        movie_queryset = Movie.objects.filter(tmdb_movie_id=99)

        self.assertTrue(movie_queryset)
        self.assertTrue(MovieList.objects.filter(movie_id=movie_queryset[0].movie_id, list_id=33))

    def test_should_create_new_movie_and_add_to_watchedlist_when_rated(self):
        result = DataBaseHandler.rate_external_movie(user_id=1, user_rating=3, tmdb_movie_id=99, tmdb_poster='bla.jpg', tmdb_title="The Amazing Papas")
        self.assertTrue(result)

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.create_list_to_user')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.create_user')
    @mock.patch('moviemancer.helpers.Helpers.get_user_id')
    def test_should_create_user_and_its_lists(self, mock_create_list_to_user, mock_create_user, mock_get_user_id):
        DataBaseHandler.register_user(name='ana', email='ana@ana', password='123')

        mock_create_list_to_user.assert_called()
        mock_create_user.assert_called()
        mock_get_user_id.assert_called()

    def test_should_return_user_id_when_registered(self):
        self.assertIsNotNone(DataBaseHandler.register_user(name='batata', email='batata@batata', password='456'))

    @mock.patch('moviemancer.models.Viwer.save')
    def test_should_create_user_if_doesent_exists(self, mock_save_viewer):
        DataBaseHandler.create_user(name='mila', email='mila@mila', password='mileumanoites')
        mock_save_viewer.assert_called()

    def test_should_return_none_if_user_already_exists(self):
        Viwer.objects.create(name='test', email='test@test', password='secure')
        self.assertIsNone(DataBaseHandler.create_user(name='test', email='test@test', password='secure'))

    @mock.patch('moviemancer.models.List.save')
    def test_should_create_list_to_user(self, mock_create_list_to_user):
        DataBaseHandler.create_list_to_user(user_id=5, type_id=3)
        mock_create_list_to_user.assert_called()

    @mock.patch('moviemancer.models.Viwer.save')
    def test_should_update_user(self, mock_update_user_info):
        DataBaseHandler.update_user_info(user_id=88, email='new@new', name='new', password='')
        mock_update_user_info.assert_called()

    def test_should_return_true_if_user_exists(self):
        DataBaseHandler.create_user(name='I exist', email='iexist@test', password='123')

        self.assertTrue(DataBaseHandler.authenticate_user(email='iexist@test', password='123'))

    def test_should_return_false_if_user_doesnt_exist(self):
        self.assertFalse(DataBaseHandler.authenticate_user(email='xuxa@test', password='**'))

    @mock.patch('moviemancer.models.Comments.save')
    def test_should_add_comment_to_movie(self, mock_save_comment):
        DataBaseHandler.add_comment(movie_tmdb_id=3, user_id=1, comment='bom!')
        mock_save_comment.assert_called()

    @mock.patch('moviemancer.models.Comments.delete')
    def test_should_delete_comment(self, mock_delete_comment):
        DataBaseHandler.delete_comment(comment_id=99)
        mock_delete_comment.assert_called()

    @mock.patch('moviemancer.models.MovieList.save')
    def test_should_add_recommendation_list_to_database(self, mock_save):
        DataBaseHandler.add_recommendation_to_database(reco_list=[2,4,6], user_id=1)
        self.assertEqual(mock_save.call_count, 3)