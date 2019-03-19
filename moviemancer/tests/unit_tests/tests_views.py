from django.test import TestCase
from moviemancer.views import *
from unittest import mock
import json

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



