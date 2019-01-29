from django.test import TestCase
from moviemancer.helpers import Helpers
from moviemancer.tests.unit_tests.database_stub import DatabaseStub

class HelpersTestCase(TestCase):
    def setUp(self):
        DatabaseStub.create_database_stub()

    def test_should_return_list_by_user(self):
        self.assertEqual(Helpers.get_user_list_id_by_type_id(user_id=1, type_id=3), 3)

    def test_should_convert_tmdb_rating_to_five(self):
        self.assertEqual(Helpers.convert_tmdb_rating(9),5)

    def test_should_convert_tmdb_rating_to_four(self):
        self.assertEqual(Helpers.convert_tmdb_rating(8.8),4)

    def test_should_format_date_to_year_only(self):
        self.assertEqual(Helpers.formate_date_to_year('2000-06-16'), '2000')

    def test_should_return_genres_separeted_by_comas(self):
        genres='18,53'
        entry = [{'id': 18, 'name': 'Drama'}, {'id': 53, 'name': 'Thriller'}]
        self.assertEqual(Helpers.get_comma_separeted_genres(genre_list = entry), genres)

    def test_should_return_true_if_movie_on_user_list(self):
        self.assertTrue(Helpers.is_movie_on_list(user_id=1, movie_id=1, type_id=1))

    def test_should_return_false_if_movie_not_on_user_list(self):
        self.assertFalse(Helpers.is_movie_on_list(user_id=2, movie_id=1, type_id=2))
