from django.test import TestCase
from moviemancer.views import *
from unittest import mock
import json

class ViewsTest(TestCase):

    def test_should_redirects_to_moviemancer(self):
        response = self.client.get('/moviemancer')
        self.assertRedirects(response, '/moviemancer/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_filters(self):
        response = self.client.get('/filters')
        self.assertRedirects(response, '/filters/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_movies(self):
        response = self.client.get('/movies')
        self.assertRedirects(response, '/movies/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_recommendation(self):
        response = self.client.get('/recommendation')
        self.assertRedirects(response, '/recommendation/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_moviedetails(self):
        response = self.client.get('/moviedetails')
        self.assertRedirects(response, '/moviedetails/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_watchedlist(self):
        response = self.client.get('/watchedlist')
        self.assertRedirects(response, '/watchedlist/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_watchlist(self):
        response = self.client.get('/watchlist')
        self.assertRedirects(response, '/watchlist/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_login(self):
        response = self.client.get('/login')
        self.assertRedirects(response, '/login/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_singup(self):
        response = self.client.get('/singup')
        self.assertRedirects(response, '/singup/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_registergenres(self):
        response = self.client.get('/registergenres')
        self.assertRedirects(response, '/registergenres/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_profile(self):
        response = self.client.get('/profile')
        self.assertRedirects(response, '/profile/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_search(self):
        response = self.client.get('/search')
        self.assertRedirects(response, '/search/', status_code=301)
        self.assertTrue(response)

    def test_should_redirects_to_notfound(self):
        response = self.client.get('/notfound')
        self.assertRedirects(response, '/notfound/', status_code=301)
        self.assertTrue(response)

    @mock.patch('moviemancer.helpers.Helpers.get_recommendation_list')
    def test_should_return_recommendations(self, mock_get_recommendation_list):
        mock_get_recommendation_list.return_value = '{1,2,3}'
        response = self.client.post(path='/getrecommendation/', content_type='application/json', data={'user_id': 32})
        mock_get_recommendation_list.assert_called()

    def test_should_return_error_for_empty_body_on_get_recommendations(self):
        response = self.client.get(path='/getrecommendation/')
        self.assertEqual(response.content, b'Error while loading recommendations')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.update_user_info')
    def test_should_update_profile(self, mock_update_user_info):
        data = {
            'user_id': 1,
            'email': 'batata@brava.com',
            'name': 'Batata',
            'password': 'potato'
        }

        response = self.client.post(path='/updateuser/', content_type='application/json', data=data)
        mock_update_user_info.assert_called()

    def test_should_return_error_for_empty_body_on_update_user(self):
        response = self.client.get(path='/updateuser/')
        self.assertEqual(response.content, b'Error while updating user')

    @mock.patch('moviemancer.helpers.Helpers.get_comments')
    def test_should_return_all_comments(self, mock_get_comments):
        data = {
            'tmdb_movie_id': 1
        }

        mock_get_comments.return_value = "{'tmdb_movie_id': 1, 'user_id': 1,'comment': 'bla'}"
        response = self.client.post(path='/getcomments/', content_type='application/json', data=data)
        mock_get_comments.assert_called()

    def test_should_return_error_for_empty_body_on_get_all_comments(self):
        response = self.client.get(path='/getcomments/')
        self.assertEqual(response.content, b'Error while retrieving comments')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_comment')
    def test_should_add_new_comment(self, mock_add_comment):
        data = {
            'tmdb_movie_id': 1,
            'user_id': 1,
            'comment': "mediocre"
        }

        response = self.client.post(path='/addcomment/', content_type='application/json', data=data)
        mock_add_comment.assert_called()

    def test_should_return_error_for_empty_body_on_add_comments(self):
        response = self.client.get(path='/addcomment/')
        self.assertEqual(response.content, b'Error while adding comment')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.delete_comment')
    def test_should_delete_comment(self, mock_delete_comment):
        data = {
            'comment_id': 1,
        }

        response = self.client.post(path='/deletecomment/', content_type='application/json', data=data)
        mock_delete_comment.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.delete_comment')
    def test_should_return_error_for_delete_fail(self, mock_delete_comment):
        data = {
            'comment_id': 1,
        }
        mock_delete_comment.return_value = False
        response = self.client.post(path='/deletecomment/', content_type='application/json', data=data)
        self.assertEqual(response.content, b'Error while deleting comment')

    def test_should_return_error_for_empty_body_on_delete_comment(self):
        response = self.client.get(path='/deletecomment/')
        self.assertEqual(response.content, b'Error while deleting comment')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.rate_movie')
    @mock.patch('moviemancer.recommendation.Recommendation.create_user_recommendation')
    def test_should_rate_movie(self, mock_rate_movie, mock_create_user_recommendation):
        data = {
            'user_id': 1,
            'movie_id': 1,
            'rate_id': 5
        }

        response = self.client.post(path='/ratemovie/', content_type='application/json', data=data)
        mock_rate_movie.assert_called()
        mock_create_user_recommendation.assert_called()

    def test_should_return_error_for_empty_body_on_rate_movie(self):
        response = self.client.get(path='/ratemovie/')
        self.assertEqual(response.content, b'Error while rating movie')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.rate_movie')
    def test_should_rate_first_movie(self, mock_rate_movie):
        data = {
            'user_id': 1,
            'movie_id': 1,
            'rate_id': 5
        }

        response = self.client.post(path='/ratefirstmovies/', content_type='application/json', data=data)
        mock_rate_movie.assert_called()

    def test_should_return_error_for_empty_body_on_rate_movie(self):
        response = self.client.get(path='/ratefirstmovies/')
        self.assertEqual(response.content, b'Error while rating movie')

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.authenticate_user')
    def test_should_return_error_for_invalid_authentication(self, mock_authenticate_user):
        data = {
            'email': 'batata@brava.com',
            'password': '*****'
        }

        mock_authenticate_user.return_value = False
        response = self.client.post(path='/authentication/', content_type='application/json', data=data)
        self.assertEqual(response.content, b'Wrong user or password')

    def test_should_return_error_for_empty_body_on_authentication(self):
        response = self.client.get(path='/authentication/')
        self.assertEqual(response.content, b'Authentication Failure: No Response Body')

    @mock.patch('moviemancer.helpers.Helpers.get_user_id_by_email')
    @mock.patch('moviemancer.helpers.Helpers.get_user')
    @mock.patch('moviemancer.recommendation.Recommendation.create_user_recommendation')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.authenticate_user')
    def test_should_return_authentication(self, mock_authenticate_user, mock_get_user_id_by_email, mock_get_user, mock_create_user_recommendation):
        data = {
            'email': 'batata@brava.com',
            'password': '*****'
        }

        mock_authenticate_user.return_value = True
        mock_get_user.return_value = "{'user':'bla'}"

        response = self.client.post(path='/authentication/', content_type='application/json', data=data)
        mock_get_user_id_by_email.assert_called()
        mock_get_user.assert_called()
        mock_create_user_recommendation.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.register_user')
    @mock.patch('moviemancer.helpers.Helpers.user_exists')
    def test_should_register_user(self, mock_user_exists, mock_register_user):
        data = {
            'name': 1,
            'email': 'batata@brava.com',
            'password': '*****'
        }

        mock_user_exists.return_value = False
        response = self.client.post(path='/registration/', content_type='application/json', data=data)
        mock_register_user.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.user_exists')
    def test_should_show_error_when_user_exists_on_registration(self, mock_user_exists):
        data = {
            'name': 1,
            'email': 'batata@brava.com',
            'password': '*****'
        }

        mock_user_exists.return_value = True
        response = self.client.post(path='/registration/', content_type='application/json', data=data)
        print('>>>>>>>>>', response)
        self.assertEqual(response.content, b'Registration Failure: User already exists')

    def test_should_return_error_for_empty_body_on_authentication(self):
        response = self.client.get(path='/registration/')
        self.assertEqual(response.content, b'Registration Failure: No Response Body')

    @mock.patch('moviemancer.helpers.Helpers.user_exists')
    def test_should_validate_user(self, mock_user_exists):
        data = {
            'email': 'batata@brava.com'
        }

        mock_user_exists.return_value = True
        response = self.client.post(path='/validateuser/', content_type='application/json', data=data)
        self.assertEqual(response.content, b'Validation Failure: User already registered')

    @mock.patch('moviemancer.helpers.Helpers.user_exists')
    def test_should_validate_user(self, mock_user_exists):
        data = {
            'email': 'batata@brava.com'
        }

        mock_user_exists.return_value = False
        response = self.client.post(path='/validateuser/', content_type='application/json', data=data)
        mock_user_exists.assert_called()

    def test_should_return_error_for_empty_body_on_validate_user(self):
        response = self.client.get(path='/validateuser/')
        self.assertEqual(response.content, b'Validation Failure: No Response Body')

    @mock.patch('moviemancer.recommendation.Recommendation.create_user_recommendation')
    @mock.patch('moviemancer.database_handlers.DataBaseHandler.rate_external_movie')
    def test_should_rate_external_movie(self, mock_rate_external_movie, mock_create_user_recommendation):
        data = {
            'user_id': 1,
            'rate_id': 3,
            'tmdb_movie_id': 4,
            'movie_poster': 'bla.png',
            'movie_title': 'Bla Returns',
        }

        mock_rate_external_movie.return_value = True
        response = self.client.post(path='/rateexternalmovie/', content_type='application/json', data=data)
        mock_rate_external_movie.assert_called()
        mock_create_user_recommendation.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_to_list')
    def test_should_add_movie_to_watchlist(self, mock_add_to_list):
        data = {
            'user_id': 1,
            'movie_id': 2
        }

        response = self.client.post(path='/addwatchlist/', content_type='application/json', data=data)
        mock_add_to_list.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_to_list_external')
    def test_should_add_movie_to_watchlist_external(self, mock_add_to_list_external):
        data = {
            'user_id': 1,
            'tmdb_movie_id': 3,
            'tmdb_movie_id': 4,
            'movie_poster': 'bla.png',
            'movie_title': 'Bla Returns',
        }
        response = self.client.post(path='/addwatchlistexternal/', content_type='application/json', data=data)
        mock_add_to_list_external.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.get_watchedlist')
    def test_should_return_watchedlist(self, mock_get_watchedlist):
        data = {
            'user_id': 1
        }

        mock_get_watchedlist.return_value = '[{1,2,3}]'
        response = self.client.post(path='/getwatchedlist/', content_type='application/json', data=data)
        mock_get_watchedlist.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_watched')
    def test_should_remove_movie_from_watched_list(self, mock_remove_watched):
        data = {
            'user_id': 1,
            'movie_id': 1
        }

        response = self.client.post(path='/removefromwatchedlist/', content_type='application/json', data=data)
        mock_remove_watched.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.remove_movie_from_list')
    def test_should_remove_movie_from_watchlist(self, mock_remove_movie_from_list):
        data = {
            'user_id': 1,
            'movie_id': 1
        }

        response = self.client.post(path='/removefromwatchlist/', content_type='application/json', data=data)
        mock_remove_movie_from_list.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.get_watchlist')
    def test_should_return_watchlist(self, mock_get_watchlist):
        data = {
            'user_id': 1
        }

        mock_get_watchlist.return_value = "[{'1': 2}]"
        response = self.client.post(path='/getwatchlist/', content_type='application/json', data=data)
        mock_get_watchlist.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.get_rated_movies')
    def test_should_return_rated_movies(self, mock_get_rated_movies):

        mock_get_rated_movies.return_value = "[{'1': 2}]"
        response = self.client.get(path='/getratedmovies/')
        mock_get_rated_movies.assert_called()

    @mock.patch('moviemancer.recommendation.Recommendation.filter_recommendation')
    def test_should_filter_recommendation(self, mock_filter_recommendation):
        data = {
            'user_id': 1,
            'minYear': 2016,
            'maxYear': 2019,
            'minRuntime': 90,
            'maxRuntime': 180,
            'language': 'pt_br',
            'genres': '1,3,4'
        }

        mock_filter_recommendation.return_value = '[1,2,3]'
        response = self.client.post(path='/filterreco/', content_type='application/json', data=data)
        mock_filter_recommendation.assert_called()