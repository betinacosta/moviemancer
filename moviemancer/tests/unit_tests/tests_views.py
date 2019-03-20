from django.test import TestCase
from moviemancer.views import *
from unittest import mock
import json
from moviemancer.database_handlers import DataBaseHandler

class ViewsTest(TestCase):

    def test_should_redirects_to_moviemancer(self):
        response = self.client.get('/moviemancer')
        self.assertRedirects(response, '/moviemancer/', status_code=301)
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

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.update_user_info')
    def test_should_return_user_profile(self, mock_update_user_info):
        data = {
            'user_id': 1,
            'email': 'batata@brava.com',
            'name': 'Batata',
            'password': 'potato'
        }

        response = self.client.post(path='/updateuser/', content_type='application/json', data=data)
        mock_update_user_info.assert_called()

    @mock.patch('moviemancer.helpers.Helpers.get_comments')
    def test_should_return_all_comments(self, mock_get_comments):
        data = {
            'tmdb_movie_id': 1
        }

        mock_get_comments.return_value = "{'tmdb_movie_id': 1, 'user_id': 1,'comment': 'bla'}"
        response = self.client.post(path='/getcomments/', content_type='application/json', data=data)
        mock_get_comments.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.add_comment')
    def test_should_add_new_comment(self, mock_add_comment):
        data = {
            'tmdb_movie_id': 1,
            'user_id': 1,
            'comment': "mediocre"
        }

        response = self.client.post(path='/addcomment/', content_type='application/json', data=data)
        mock_add_comment.assert_called()

    @mock.patch('moviemancer.database_handlers.DataBaseHandler.delete_comment')
    def test_should_add_new_comment(self, mock_delete_comment):
        data = {
            'comment_id': 1,
        }

        response = self.client.post(path='/deletecomment/', content_type='application/json', data=data)
        mock_delete_comment.assert_called()